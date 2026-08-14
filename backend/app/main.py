from fastapi import FastAPI

from .core import setup_logger
from .services import Transcriber, Downloader
from .models import TranscriptionRequest

setup_logger()

app = FastAPI(
    title="Trans-Script API",
    version="0.1.0",
)

@app.get("/")
def welcome():
    return {"message": "Welcome to the Trans-Script API !"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post('/transcription')
def transcription(request: TranscriptionRequest):
    path = Downloader().download_audio(url=request.url)

    try:
        result = Transcriber().transcribe(audio_path=path, language=request.language)
        return result
    finally:
        path.unlink(missing_ok=True)
