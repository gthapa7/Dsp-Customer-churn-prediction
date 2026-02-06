# Customer Churn Prediction Pipeline

## Overview
End-to-end ML system for telecom customer churn prediction. The project covers data ingestion, preprocessing, model training, evaluation, and batch/real-time inference. Orchestration is handled with Apache Airflow, predictions are served through FastAPI, and a Streamlit UI provides interactive access. A Postgres database and Grafana dashboards support monitoring and reporting.

## Highlights
- Automated data ingestion and validation workflow
- Feature engineering and supervised model training
- Model evaluation with classification metrics
- FastAPI service for real-time inference
- Streamlit dashboard for interactive predictions
- Airflow DAGs for scheduled training and batch scoring
- Docker Compose setup for reproducible deployment
- Postgres and Grafana for monitoring and analytics

## Tech Stack
- Python, Pandas, scikit-learn
- FastAPI, Uvicorn
- Apache Airflow
- Streamlit
- Postgres
- Docker and Docker Compose
- Grafana

## Project Structure
```
app/                 # API, training, database utilities, Streamlit UI
airflow/             # DAGs, logs, plugins, and Airflow runtime data
data/                # Raw and prepared datasets
models/              # Trained model artifacts
monitoring/          # Grafana dashboards and configs
docker-compose.yml   # Multi-service deployment
Dockerfile           # API container build
requirements.txt     # Python dependencies
```

## Quick Start (Docker Compose)
Prerequisites: Docker Desktop running on macOS.

```bash
docker compose up -d --build
```

Services:
- FastAPI: http://localhost:8000
- Streamlit: http://localhost:8501
- Airflow: http://localhost:8080 (admin / admin)
- Grafana: http://localhost:3000 (admin / admin)

## API Usage
Example inference request:

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{ "features": { "tenure": 12, "monthly_charges": 70.5, "contract": "Month-to-month" } }'
```

## Airflow Pipeline
DAGs handle:
1. Data ingestion from incoming CSV batches
2. Preprocessing and feature encoding
3. Model training and evaluation
4. Batch inference and output persistence

## Model Evaluation
The pipeline reports standard classification metrics:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## Notes for Reviewers
- The repo is designed for reproducible, containerized execution.
- The pipeline is modular and easy to extend with new features or models.
- Airflow provides traceable, repeatable workflows suitable for production MLOps.

## Author
Ganesh Bahadur Thapa





