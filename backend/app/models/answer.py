from pydantic import BaseModel

class Segment(BaseModel):
    start: float
    end: float
    text: str

class TranscriptionAnswer(BaseModel):
    language: str
    text: str
    segments: list[Segment]