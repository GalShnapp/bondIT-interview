from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class FlightBase(BaseModel):
    arrival_time: Optional[datetime]
    departure_time: Optional[datetime]


class FlightCreate(FlightBase):
    pass


class Flight(FlightBase):
    arrival_time: datetime
    departure_time: datetime
    id: str
    success: bool = False