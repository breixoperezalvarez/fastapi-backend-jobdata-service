from fastapi import FastAPI, Query

from app.data_loader import load_jobs
from app.filters import filter_jobs
from app.stats import get_basic_stats, get_city_stats, get_source_stats

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

    return {
        "count": len(filtered),
        "jobs": filtered.head(limit).to_dict(orient="records"),
    }

@app.get("/stats")
def stats():
    df = load_jobs()
    return get_basic_stats(df)