from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import datasets, algorithms, runs, metrics, jobs, system, network, uploads
from app.core.database import init_db

app = FastAPI(
    title="GRNBenchFlow API",
    version="1.0.0",
    description="Backend for GRNBenchFlow – a benchmarking and GRN visualization platform built on BEELINE."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(datasets.router, prefix="/datasets", tags=["Datasets"])
app.include_router(algorithms.router, prefix="/algorithms", tags=["Algorithms"])
app.include_router(runs.router, prefix="/runs", tags=["Runs"])
app.include_router(metrics.router, prefix="/metrics", tags=["Metrics"])
app.include_router(network.router, prefix="/network", tags=["Network"])
app.include_router(uploads.router, prefix="/uploads", tags=["Uploads"])
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
app.include_router(system.router, prefix="/system", tags=["System"])

@app.on_event("startup")
async def startup():
    await init_db()

@app.get("/")
def root():
    return {"message": "GRNBenchFlow API running"}
