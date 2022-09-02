import config
import logging
from models.car import Car 
from helpers.emailclient  import EMailClient
from helpers.ftpclient import FTPClient

logger = logging.getLogger() # root


def main():
    car1 = Car("AA12345")
    print(car1)
    
    print(config.app_var["apptitle"])
    
    # Create an Instance
    hotmail_client = EMailClient("hotmail")
    
    gmail_client = EMailClient("gmail")
    
    email_client = EMailClient()
    
    

if __name__  == "__main__":
    logger.info("Application is started")
    main()



