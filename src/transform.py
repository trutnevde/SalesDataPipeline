import pandas as pd
import logging

from config.settings import RAW_DATA_PATH, CLEANED_DATA_PATH

def clean_and_transform_data():
    logger = logging.getLogger(__name__)
    logger.info("Starting transformation...")

    df = pd.read_csv(RAW_DATA_PATH)


    df.rename(columns={"price": "unit_price"}, inplace=True)
    df["quantity"] = 1
    df["total_sales"] = df["unit_price"] * df["quantity"]


    df.to_csv(CLEANED_DATA_PATH, index=False)
    logger.info(f"Cleaned data saved to {CLEANED_DATA_PATH}")