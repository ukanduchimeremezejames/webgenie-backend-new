import time, uuid
from app.core.database import AsyncSessionLocal
from app.models.run import Run

async def run_algorithm(dataset_id, algorithm_id, params):
    run_id = str(uuid.uuid4())
    start = time.time()
    time.sleep(1)
    runtime = time.time() - start

    async with AsyncSessionLocal() as db:
        db.add(Run(run_id=run_id, dataset_id=dataset_id, algorithm_id=algorithm_id,
                   parameters_json=params, runtime_seconds=runtime, memory_mb=128, provenance_hash="stub-run"))
        await db.commit()

    return {"run_id": run_id, "runtime": runtime}
