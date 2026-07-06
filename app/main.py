from fastapi import FastAPI


app = FastAPI(
    title = "Enterprise Data Analytics API",
    description = "A professional API for data analytics, reorting, and dataset processing",
    version = "1.0.0"
) 


@app.get("/") 
def home():
    return {
        "message" : "Welcome to Enterprise Data Analytics API",
        "status" : "running",
        "version" : "1.0.0"
    }
    

@app.get("/health")
def health_check():
    return {
        "status" : "healthy",
        "service" : "Enterrisse Data Analytics API"
    }