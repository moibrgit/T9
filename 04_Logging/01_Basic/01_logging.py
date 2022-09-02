import os 
from pathlib import Path 
import logging 


os.chdir(Path(__file__).parent)

logging.basicConfig(filename="app.log", level=logging.INFO,
                    format='%(name)s - %(levelname)s - %(asctime)s- %(filename)s- %(message)s')



def add(x, y):
    total = x + y 
    logging.debug(str(total))
    
    return total 


total = add(70,6)
print("The total is:", total)

logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")
logging.exception("This is a exception message")


