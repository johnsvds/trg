from models.coordinates import Coordinates
from pydantic import BaseModel

class Root(BaseModel):
    start: Coordinates
    finish: Coordinates