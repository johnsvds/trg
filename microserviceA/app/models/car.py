from enum import Enum

import json
from pydantic import BaseModel


class CarStatus(int, Enum):
    UNAVAILABLE = 0
    AVAILABLE = 1

class Car(BaseModel):     
    car_id:str  
    brand: str
    model: str
    license_plate:str
    status: CarStatus
 
    