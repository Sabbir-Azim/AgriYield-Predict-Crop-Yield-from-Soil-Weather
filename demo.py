from AgriYield.logger import logging
from AgriYield.exception import AgriYieldException
import sys

try:
    1/0
except Exception as e:
    logging.info("Dividing by zero")
    raise AgriYieldException("Error occurred", sys) from e