import logging
logger = logging.getLogger() # root


class Car:
    
    def __init__(self, kz) -> None:
        self.kz = kz 
        logger.debug("Car instance is created")
        
        
    def __repr__(self) -> str:
        return f"KZ: {self.kz}"