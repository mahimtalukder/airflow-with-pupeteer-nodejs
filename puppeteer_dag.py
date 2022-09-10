from datetime import datetime, timedelta
import time
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from airflow import DAG
from airflow.operators.python import PythonOperator
import os


default_args = {
    'owner': 'clickSpikes',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def scap():
    os.system("npm start")

with DAG(
    dag_id = "puppeteer_v2",
    default_args = default_args,
    description = "Tesing the python operator",
    start_date = datetime(2022, 9, 9, 21),
    schedule_interval = "@daily"
) as dag:
    puppeteer = PythonOperator(
        task_id='greet',
        python_callable=scap
    )

    puppeteer
