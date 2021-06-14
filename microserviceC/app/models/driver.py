import json
from app.models.car import Car
from pydantic import BaseModel

class Driver(BaseModel):
    driver_id:str
    penalty:int=0