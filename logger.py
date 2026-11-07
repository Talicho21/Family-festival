import logging
import os
from config import Config

os.makedirs(Config.LOG_FOLDER, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(Config.LOG_FOLDER, "bot.log"), encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("photo_bot")