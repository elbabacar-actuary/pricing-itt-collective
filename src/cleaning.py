import pandas as pd

def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df

def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # Example: remove fully empty rows
    df = df.dropna(how="all")
    return df
