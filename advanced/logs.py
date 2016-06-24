import logging
from logging import handlers

logging.basicConfig(level=logging.DEBUG)
logger = logging.root
logger.setLevel(logging.DEBUG)
handler = handlers.TimedRotatingFileHandler(
    'log', 'H', 24, 7)
handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s %(lineno)d %(message)s'))
logger.addHandler(handler)

getLogger = logging.getLogger
