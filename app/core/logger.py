import logging 
from app.core.config import get_settings

settings= get_settings()

def setup_logger():
    logger = logging.getLogger("CLARIX")
    if settings.environment.lower() == "development":
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s: %(lineno)d |  %(message)s" )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger= setup_logger()

if __name__ == "__main__":
    logger.debug("This is a DEBUG message")
    logger.info("This is an INFO message")
    logger.warning("This is a WARNING message")
    logger.error("This is an ERROR message")