import os 
from pathlib import Path 
import logging 
import json 
from logging.config import fileConfig

# Main Paths
FILE_LOG_INI = "./logging.ini"
CONFIG_JSON = "./config.json"



os.chdir(Path(__file__).parent)
fileConfig(FILE_LOG_INI, disable_existing_loggers=False)
logger = logging.getLogger() # root

# Read config JSON
with open(CONFIG_JSON, mode = "r", encoding="UTF-8") as file:
    content = file.read() 
app_var = json.loads(content)  


# Credentials EMail
email_username = app_var["email"]["username"]
email_password = app_var["email"]["password"]
smtp_server = app_var["email"]["smtp_server"]
smtp_port = app_var["email"]["smtp_port"]


logger.info("System config is successfully executed.!")

 