from pydantic import BaseModel
from datetime import datetime


class FlightBase(BaseModel):
    arrival_time: datetime
    departure_time: datetime


class FlightCreate(FlightBase):
    pass


class Flight(FlightBase):
    id: str
    success: bool

    def to_csv_row(self):
        return [self.id, self.arrival_time, self.departure_time, self.success]