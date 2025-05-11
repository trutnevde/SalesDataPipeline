import pandas as pd
import os
import pytest

from src.transform import clean_and_transform_data

def test_cleaning_creates_total_sales_column(tmpdir):
    test_raw_path = tmpdir.join("test_raw.csv")
    test_cleaned_path = tmpdir.join("test_cleaned.csv")

    df = pd.DataFrame({"price": [100, 200]})
    df.to_csv(test_raw_path, index=False)


    from config.settings import set_paths
    set_paths(raw=test_raw_path, cleaned=test_cleaned_path)

    clean_and_transform_data()

    result_df = pd.read_csv(test_cleaned_path)
    assert "total_sales" in result_df.columns