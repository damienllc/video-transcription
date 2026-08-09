import logging

from yt_dlp import YoutubeDL

logger = logging.getLogger(__name__)

class Downloader: 
    def download_audio(self, url: str, output_dir: str):
        logger.info("Starting download: %s", url)
        options = {
            "format": "bestaudio/best",
            "outtmpl": f"{output_dir}/%(id)s.%(ext)s",
            "noplaylist": True,
        }

        try:
            with YoutubeDL(options) as ydl:
                ydl.download([url])

        except Exception:
            logger.exception("Download failed")
            raise
