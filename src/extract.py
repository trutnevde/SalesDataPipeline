import pandas as pd
import requests
import os

from config.settings import RAW_DATA_PATH

def fetch_sales_data_from_api():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    df = pd.DataFrame(response.json())
    df.to_csv(RAW_DATA_PATH, index=False)
    print(f"Raw data saved to {RAW_DATA_PATH}")