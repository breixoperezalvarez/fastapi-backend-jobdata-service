from fastapi import FastAPI, Query

from app.data_loader import load_jobs
from app.filters import filter_jobs
from app.stats import get_basic_stats, get_city_stats, get_source_stats
from app.cleaning import clean_html_text, shorten_text

app = FastAPI(
    title="Job Data Backend API",
    description="FastAPI backend service for serving and filtering job data.",
    version="1.0.0",
)

@app.get("/")
def home():
    return {"message": "API is now working"}

@app.get("/jobs")
def get_jobs(
        city: str | None = None,
        remote: bool | None = None,
        keyword: str | None = None,
        source: str | None = None,
        limit: int = Query(default=20, ge=1, le=100)
):
    df = load_jobs()
    filtered = filter_jobs(df, city, remote, keyword, source)

    jobs = filtered.head(limit).copy()

    if "description" in jobs.columns:
        jobs["description_preview"] = jobs["description"].apply(
            lambda text: shorten_text(clean_html_text(text))
        )
        jobs = jobs.drop(columns=["description"])

    return {
        "count": int(len(filtered)),
        "jobs": jobs.to_dict(orient="records"),
    }

@app.get("/stats")
def stats():
    df = load_jobs()
    return get_basic_stats(df)