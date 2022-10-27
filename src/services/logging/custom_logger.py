from loguru import logger
from src.config import LOG_FILE


logger.add(LOG_FILE)
