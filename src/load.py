import pandas as pd
from config.settings import CLEANED_DATA_PATH, OUTPUT_EXCEL_PATH

def save_to_excel():
    df = pd.read_csv(CLEANED_DATA_PATH)
    df.to_excel(OUTPUT_EXCEL_PATH, index=False)
    print(f"Data saved to Excel: {OUTPUT_EXCEL_PATH}")