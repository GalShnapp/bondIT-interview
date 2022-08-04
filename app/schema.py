from pydantic import BaseModel
from datetime import datetime


class FlightBase(BaseModel):
    id: str
    arrival_time: datetime
    departure_time: datetime


class FlightCreate(FlightBase):
    pass


class Flight(FlightBase):
    success: bool = False