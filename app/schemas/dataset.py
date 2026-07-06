from pydantic import BaseModel

class DatasetCreate(BaseModel):
    name : str
    category : str
    rows : int

class DatasetResponse(BaseModel):
    id : int
    name : str
    category : str
    rows : int
    status : str