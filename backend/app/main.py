from fastapi import FastAPI

from backend.app.core.logger import setup_logger


setup_logger()

app = FastAPI(
    title="Video Transcriber API",
    version="0.1.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}