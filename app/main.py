from fastapi import FastAPI

from app.routers import health, datasets

app = FastAPI(
    title = "Enterprise Data Analytics API",
    description = "Professional Data Analytics Backend",
    version = "1.0.0"
) 


@app.get("/") 
def home():
    return {
        "message" : "Welcome to Enterprise Data Analytics API",
        "status" : "running"
    }




app.include_router(health.router)
app.include_router(datasets.router)
    

