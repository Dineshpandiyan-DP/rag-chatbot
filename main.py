from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_route():
    return {"message":"RAG API is Running"}

@app.get("/health")
def get_health():
    return {"status": "ok","app": "CLARIX","version": "1.0.0"}