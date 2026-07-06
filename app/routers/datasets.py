from fastapi import APIRouter

router = APIRouter()

@router.get("/datasets/{dataset_id}")

def get_dataset(dataset_id : int):
    return {
        "datasetid" : dataset_id,
        "message" : f"Dataset {dataset_id} details will be shown here"
    }

@router.get("/datasets")
def list_datasets(limit : int = 10, category : str | None = None):
    return {
        "limit" : limit,
        "category" : category,
        "message" : "Dataset list will be shown here"
    }