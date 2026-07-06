from fastapi import APIRouter

from app.schemas.dataset import DatasetCreate, DatasetResponse

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

@router.post("/datasets", response_model = DatasetResponse) # This validates and documents the response body
def create_dataset(dataset : DatasetCreate): #This validates the request body
    return {
        "id" : 1,
        "name" : dataset.name,
        "category" : dataset.category,
        "rows" : dataset.rows,
        "status" : "created"
    }