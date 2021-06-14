from enum import Enum
from pydantic import BaseModel
import json



class DriverStatus(int, Enum):
    UNAVAILABLE = 0
    AVAILABLE = 1

class Driver(BaseModel):
    driver_id:str
    first_name: str 
    last_name: str 
    license_number:str
    status: DriverStatus