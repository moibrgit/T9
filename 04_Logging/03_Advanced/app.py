import os 
from pathlib import Path 
import logging 
from logging.config import fileConfig

os.chdir(Path(__file__).parent)

fileConfig("./logging.ini", disable_existing_loggers=False)

logger = logging.getLogger()

logger.info("This is a test message")

