from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/filtered_jobs.csv")


def load_jobs() -> pd.DataFrame:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Data file not found: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)
    return df.fillna("")