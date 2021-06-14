from pydantic import BaseModel
class Coordinates(BaseModel):
    lon:float
    lat:float