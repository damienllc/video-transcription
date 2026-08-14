import logging

from faster_whisper import WhisperModel
from app.models import TranscriptionAnswer

logger = logging.getLogger(__name__)

class Transcriber:
    def __init__(
        self,
        model_size: str = "small",
        device: str = "cpu",
        compute_type: str = "int8",
    ):
        logger.info(
            "Loading Whisper model: %s (%s / %s)",
            model_size,
            device,
            compute_type,
        )

        self.model = WhisperModel(
            model_size,
            device=device,
            compute_type=compute_type,
        )

        logger.info("Whisper model loaded")

    def transcribe(self, audio_path: str, language: str) -> TranscriptionAnswer:
        logger.info("Starting transcription: %s", audio_path)

        try:
            segments, info = self.model.transcribe(audio=audio_path, language=language)

            result_segments = []

            for segment in segments:
                result_segments.append({
                    "start": segment.start,
                    "end": segment.end,
                    "text": segment.text.strip(),
                })

            text = " ".join(
                segment["text"]
                for segment in result_segments
            )

            logger.info(
                "Transcription completed: language=%s",
                info.language
            )

            return TranscriptionAnswer(
                language=info.language,
                text=text,
                segments=result_segments,
            )

        except Exception:
            logger.exception("Transcription failed")
            raise