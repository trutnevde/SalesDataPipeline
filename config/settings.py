

import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(PROJECT_ROOT, "data")
RAW_DATA_PATH = os.path.join(DATA_DIR, "raw", "sales_raw.csv")
CLEANED_DATA_PATH = os.path.join(DATA_DIR, "processed", "cleaned_sales.csv")

OUTPUT_EXCEL_PATH = os.path.join(PROJECT_ROOT, "reports", "sales_report.xlsx")

os.makedirs(os.path.join(DATA_DIR, "raw"), exist_ok=True)
os.makedirs(os.path.join(DATA_DIR, "processed"), exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, "reports"), exist_ok=True)

LOGS_DIR = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(LOGS_DIR, exist_ok=True)