import os, json, uuid
from git import Repo
from datetime import datetime
from app.core.config import settings
from app.core.database import AsyncSessionLocal
from app.models.dataset import Dataset
from app.models.algorithm import Algorithm

BEELINE_URL = settings.BEELINE_REPO_URL
CLONE_DIR = settings.CLONE_DIR

async def sync_beeline():
    if not os.path.exists(CLONE_DIR):
        Repo.clone_from(BEELINE_URL, CLONE_DIR)
    else:
        repo = Repo(CLONE_DIR)
        repo.remotes.origin.pull()

    dataset_dir = os.path.join(CLONE_DIR, "datasets")
    datasets = []
    if os.path.exists(dataset_dir):
        for d in os.listdir(dataset_dir):
            meta_path = os.path.join(dataset_dir, d, "metadata.json")
            if not os.path.exists(meta_path):
                continue
            with open(meta_path, "r") as f:
                meta = json.load(f)
            datasets.append({
                "dataset_id": str(uuid.uuid4()),
                "name": meta.get("name", d),
                "organism": meta.get("organism"),
                "type": meta.get("type"),
                "genes": meta.get("num_genes"),
                "cells": meta.get("num_samples"),
                "edges": meta.get("num_edges"),
                "source": "beeline",
                "last_updated": datetime.now()
            })

    async with AsyncSessionLocal() as db:
        for ds in datasets:
            db.add(Dataset(**ds))
        await db.commit()

    algo_dir = os.path.join(CLONE_DIR, "algorithms")
    algorithms = []
    if os.path.exists(algo_dir):
        for a in os.listdir(algo_dir):
            algorithms.append({
                "algorithm_id": str(uuid.uuid4()),
                "name": a,
                "version": "1.0",
                "source_url": f"{BEELINE_URL}/tree/master/algorithms/{a}",
                "description": f"BEELINE algorithm {a}"
            })

    async with AsyncSessionLocal() as db:
        for alg in algorithms:
            db.add(Algorithm(**alg))
        await db.commit()

    return {"datasets_imported": len(datasets), "algorithms_imported": len(algorithms)}
