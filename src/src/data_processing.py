"""
Aircraft Maintenance Reliability Analysis
Data Processing Module
"""

import pandas as pd


def load_data(file_path):
    """
    Load aircraft maintenance data from a CSV file.
    """
    return pd.read_csv(file_path)


def clean_data(df):
    """
    Perform basic data cleaning.
    """

    df = df.copy()

    # Remove duplicate records
    df = df.drop_duplicates()

    # Remove completely empty rows
    df = df.dropna(how="all")

    return df


def basic_summary(df):
    """
    Generate basic statistical summary.
    """
    return df.describe(include="all")


if __name__ == "__main__":
    print("Aircraft maintenance data processing module is ready.")
