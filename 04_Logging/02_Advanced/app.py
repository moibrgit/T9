import os 
from pathlib import Path 
import logging 


os.chdir(Path(__file__).parent)

 
 
# Create a logger

logger = logging.getLogger()  # root logger
logger.setLevel(logging.WARNING)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(asctime)s- %(filename)s- %(message)s')
 
 
# 1. File Handler Logger
file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)


# 2. Stream Handler -> in terminal
stream_handler = logging.StreamHandler()
 
 
# Add handler to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
 
 


logger.debug("Hello advanced logger debug")
logger.info("Hello advanced logger info")
logger.error("Hello advanced logger error")

 
 
 

# def add(x, y):
#     total = x + y 
#     logging.debug(str(total))
    
#     return total 
 


