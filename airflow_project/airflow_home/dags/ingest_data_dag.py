from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import random
import shutil

# Folder paths (update if needed)
RAW_FOLDER = "/Users/ganeshbahadurthapa/Desktop/DSP-Project/airflow_project/raw-data"
GOOD_FOLDER = "/Users/ganeshbahadurthapa/Desktop/DSP-Project/airflow_project/good-data"

def read_data():
    """Select up to 5 random CSV files from raw-data and return their paths."""
    all_files = [f for f in os.listdir(RAW_FOLDER) if f.endswith(".csv")]
    if not all_files:
        print("❌ No CSV files found in raw-data folder.")
        return []

    # Pick up to 5 random files
    files_to_move = random.sample(all_files, min(5, len(all_files)))
    full_paths = [os.path.join(RAW_FOLDER, f) for f in files_to_move]

    print(f"📂 Selected {len(full_paths)} files to move: {files_to_move}")
    return full_paths  # stored in XCom

def save_files(ti):
    """Move the selected files from raw-data to good-data."""
    file_paths = ti.xcom_pull(task_ids='read_data')
    if not file_paths:
        print("⚠️ No files to move.")
        return

    moved_files = []
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        dest_path = os.path.join(GOOD_FOLDER, file_name)
        try:
            shutil.move(file_path, dest_path)
            moved_files.append(file_name)
            print(f"✅ Moved: {file_name}")
        except Exception as e:
            print(f"❌ Error moving {file_name}: {e}")

    print(f"✨ Successfully moved {len(moved_files)} file(s): {moved_files}")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 10, 11),
}

with DAG(
    dag_id='ingestion_dag',
    default_args=default_args,
    description='Moves up to 5 random CSVs from raw-data to good-data per run',
    schedule_interval=None,
    catchup=False,
    tags=['data_ingestion']
) as dag:

    read_task = PythonOperator(
        task_id='read_data',
        python_callable=read_data
    )

    save_task = PythonOperator(
        task_id='save_files',
        python_callable=save_files
    )

    read_task >> save_task
