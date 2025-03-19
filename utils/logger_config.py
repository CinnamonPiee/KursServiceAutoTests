import logging
import os
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_logger(page_name: str):
    """Создаёт логгер, который пишет логи в logs/<page_name>/<YYYY-MM-DD>/log.log"""

    current_date = datetime.now().strftime("%Y-%m-%d")

    log_dir = os.path.join(BASE_DIR, "logs", page_name, current_date)
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "tests.log")

    logger = logging.getLogger(f"{page_name}_{current_date}")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )

        logger.addHandler(file_handler)

    return logger