import logging

from faster_whisper import WhisperModel

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

    def transcribe(self, audio_path: str):
        logger.info("Starting transcription: %s", audio_path)

        try:
            segments, info = self.model.transcribe(audio_path)

            logger.info(
                "Transcription completed: language=%s",
                info.language
            )

            return segments, info

        except Exception:
            logger.exception("Transcription failed")
            raise