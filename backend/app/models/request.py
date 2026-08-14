from pydantic import BaseModel

class TranscriptionRequest(BaseModel):
    url: str
    language: str | None = None