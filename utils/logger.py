import logging
import os
from datetime import datetime


def get_logger(name="TestLogger", level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False

    # Check if handlers are already added to avoid duplicates
    if not logger.handlers:
        os.makedirs("logs", exist_ok=True)

        # Creating a unique log file per run
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f"logs/test_run_{timestamp}.log"

        file_handler = logging.FileHandler(log_filename)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)

        # Adding logs to stdout
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
