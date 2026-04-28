import pandas as pd


def get_basic_stats(df: pd.DataFrame) -> dict:
    return {
        "total_jobs": int(len(df)),
        "remote_jobs": int(df["remote"].sum()),
        "onsite_jobs": int((df["remote"] == False).sum()),
        "unique_sources": int(df["source"].nunique()),
        "unique_locations": int(df["location"].nunique()),
    }


def get_city_stats(df: pd.DataFrame) -> dict:
    return df["location"].value_counts().to_dict()


def get_source_stats(df: pd.DataFrame) -> dict:
    return df["source"].value_counts().to_dict()