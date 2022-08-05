from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .csv_utils import DATA_FILE_DATE_FORMAT, csv_date_to_dateime


class FlightBase(BaseModel):
    arrival_time: Optional[datetime]
    departure_time: Optional[datetime]


class FlightCreate(FlightBase):
    pass


class Flight(FlightBase):
    arrival_time: datetime
    departure_time: datetime
    id: str = "NoIDAvailable"
    success: bool = False