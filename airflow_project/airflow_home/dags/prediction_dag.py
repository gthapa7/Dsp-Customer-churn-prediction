from airflow import DAG
from airflow.operators.python import PythonOperator, ShortCircuitOperator
from datetime import datetime
import os
import requests

GOOD_FOLDER = "/Users/ganeshbahadurthapa/Desktop/DSP-Project/airflow_project/good-data"
MODEL_API_URL = "http://localhost:5000/predict"  # Replace with your real endpoint

def check_for_new_data(ti):
    """Check if there are any files in good-data."""
    files = [os.path.join(GOOD_FOLDER, f) for f in os.listdir(GOOD_FOLDER) if f.endswith(".csv")]
    if not files:
        print("No new files found in good-data folder.")
        return False  # Skip downstream tasks
    print(f"Found {len(files)} new file(s): {files}")
    ti.xcom_push(key='new_files', value=files)
    return True

def make_predictions(ti):
    """Send each file to the model API for prediction."""
    files = ti.xcom_pull(task_ids='check_for_new_data', key='new_files')
    if not files:
        print("No files passed for prediction.")
        return

    for file_path in files:
        print(f"Making prediction for: {file_path}")
        try:
            with open(file_path, 'rb') as f:
                # Replace with actual API endpoint and logic
                response = requests.post(MODEL_API_URL, files={'file': f})
                print(f"Response for {os.path.basename(file_path)}: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Error making prediction for {file_path}: {e}")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 10, 11),
}

with DAG(
    dag_id='prediction_dag',
    default_args=default_args,
    description='Checks for new data in good-data and makes predictions',
    schedule_interval=None,
    catchup=False,
    tags=['prediction']
) as dag:

    check_task = ShortCircuitOperator(
        task_id='check_for_new_data',
        python_callable=check_for_new_data
    )

    predict_task = PythonOperator(
        task_id='make_predictions',
        python_callable=make_predictions
    )

    check_task >> predict_task
