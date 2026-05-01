import logging
def setup_logger():
    logger = logging.getLogger("zecpath_ai")
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler("ai_logs.log")
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
logger = setup_logger()