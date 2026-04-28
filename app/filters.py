import pandas as pd


def filter_jobs(
    df: pd.DataFrame,
    city: str | None = None,
    remote: bool | None = None,
    keyword: str | None = None,
    source: str | None = None,
) -> pd.DataFrame:
    result = df.copy()

    if city:
        result = result[result["location"].str.contains(city, case=False, na=False)]

    if remote is not None:
        result = result[result["remote"] == remote]

    if keyword:
        keyword_mask = (
            result["title"].str.contains(keyword, case=False, na=False)
            | result["company"].str.contains(keyword, case=False, na=False)
        )
        result = result[keyword_mask]

    if source:
        result = result[result["source"].str.contains(source, case=False, na=False)]

    return result