from fastapi import FastAPI

from .core import setup_logger

setup_logger()

app = FastAPI(
    title="Video Transcriber API",
    version="0.1.0",
)

@app.get("/")
def welcome():
    return {"message": "Welcome !"}

@app.get("/health")
def health():
    return {"status": "ok"}