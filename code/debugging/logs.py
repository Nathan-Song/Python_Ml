import logging
from logging.handlers import RotatingFileHandler

# logging.basicConfig(filename="app.log",
#                     format='%(asctime)s: %(levelname)s: %(message)s',
#                     level=logging.ERROR)

logger = logging.getLogger("app_logger")
logger.setLevel(logging.DEBUG)

info_handler = RotatingFileHandler("info.log",  maxBytes=1, backupCount=5)
info_handler.setLevel(logging.INFO)

error_handler = logging.FileHandler("errors.log")
error_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')

info_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

logger.addHandler(info_handler)
logger.addHandler(error_handler)


def divide(x, y):
    logger.info(f"add: {x} + {y}")
    return x / y


try:
    divide(2, 0)
except:
    logger.critical("Tried to divide by zero")
