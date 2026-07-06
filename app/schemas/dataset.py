from pydantic import BaseModel

class Dataset(BaseModel):
    name : str
    category : str
    rows : int
