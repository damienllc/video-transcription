import logging
import yt_dlp

from pathlib import Path
from app.config import DOWNLOAD_DIR

logger = logging.getLogger(__name__)

class Downloader: 
    def download_audio(self, url: str):
        DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

        output_template = str(DOWNLOAD_DIR / "%(title)s.%(ext)s")
        
        logger.info("Starting download: %s", url)

        options = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "wav",
                }
            ],
        }

        try:
            with yt_dlp.YoutubeDL(options) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)

            logger.info("Download success !")
            return Path(filename).with_suffix(".wav")

        except Exception:
            logger.exception("Download failed")
            raise
