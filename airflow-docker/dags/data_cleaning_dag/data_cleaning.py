import numpy as np
import pandas as pd

from datetime import timedelta
import airflow
import os

from airflow import DAG
from airflow.operators.python import PythonOperator

dag_path = os.getcwd()
