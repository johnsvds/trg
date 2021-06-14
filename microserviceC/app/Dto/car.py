import json
from app.models.coordinates import Coordinates
from pydantic import BaseModel

class CarDTO(BaseModel):
    speed:float
    position: Coordinates
    