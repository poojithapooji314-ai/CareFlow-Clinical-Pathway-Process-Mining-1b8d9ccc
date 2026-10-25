
from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")

def inspect_csv(file_path):
    df = pd.read_csv(file_path)

    print("Rows:", len(df))
    print("Columns:", list(df.columns))
    print("\nMissing values:")
    print(df.isna().sum())
    print("\nDuplicate rows:", df.duplicated().sum())

    return df

if __name__ == "__main__":
    print("CareFlow data validation starter")
    print("Place an authorized CSV event log in data/")
    print("Confirm case ID, activity, and timestamp column names")
    print("before running the analysis.")
