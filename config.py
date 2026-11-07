import os
from pathlib import Path
from dotenv import load_dotenv

# Base directory for the project (always absolute)
BASE_DIR = Path(__file__).resolve().parent

# Explicitly load .env from the project directory
load_dotenv(BASE_DIR / ".env")


class Config:
    BASE_DIR = BASE_DIR

    # Telegram Bot Token
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    # Project folders
    DOWNLOAD_FOLDER = str(BASE_DIR / "downloads")
    OUTPUT_FOLDER = str(BASE_DIR / "output")
    OVERLAY_PATH = str(BASE_DIR / "assets" / "overlay.png")
    LOG_FOLDER = str(BASE_DIR / "logs")

    # Font
    FONT_PATH = str(BASE_DIR / "fonts" / "NotoSansEthiopic-Regular.ttf")

    # Text
    TEXT = "እኔም እገኛለሁ"
    FONT_SIZE = 70

    # Gradient
    GRADIENT_COLOR = (120, 30, 255)
    GRADIENT_ALPHA = 120