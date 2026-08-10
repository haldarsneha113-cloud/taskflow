from fastapi import FastAPI
from pydantic import BaseModel
from backend.algorithms import (
    insertion_sort_count,
    binary_search_count,
    linear_search_count,
)

app = FastAPI(title="Capstone Project API")

class SortRequest(BaseModel):
    records: list[dict]
    key: str

class SearchRequest(BaseModel):
    records: list[dict]
    target: str | int
    key: str

@app.get("/")
def read_root():
    return {"message": "Capstone API is running"}

@app.post("/sort")
def run_sort(data: SortRequest):
    records = [dict(r) for r in data.records]
    comparisons = insertion_sort_count(records, data.key)
    return {"sorted_records": records, "comparisons": comparisons}

@app.post("/search/binary")
def run_binary_search(data: SearchRequest):
    result = binary_search_count(data.records, data.target, data.key)
    return result

@app.post("/search/linear")
def run_linear_search(data: SearchRequest):
    result = linear_search_count(data.records, data.target, data.key)
    return result
