from fastapi import FastAPI

from app.routers import health

app = FastAPI(
    title = "Enterprise Data Analytics API",
    description = "Professional Data Analytics Backend",
    version = "1.0.0"
) 

app.include_router(health.router)

@app.get("/") 
def home():
    return {
        "message" : "Welcome to Enterprise Data Analytics API",
        "status" : "running"
    }
    

