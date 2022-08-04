from fastapi import FastAPI, HTTPException
from .schema import Flight, FlightCreate
from .crud import _get_flight, _upsert_flight, get_todays_flight_count

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/flights/{flight_id}")
async def get_flight(flight_id):
    flight = _get_flight(flight_id)
    if flight is None:
        raise HTTPException(status_code=404, detail=f"flight {flight_id} not found")
    return flight


def is_successful_flight(flight:Flight) -> bool:
    flight_count = get_todays_flight_count()
    minutes = ((flight.departure_time - flight.arrival_time).total_seconds()/60)
    return minutes > 180 and flight_count < 20


@app.put("/flights/{flight_id}", response_model=Flight)
async def upsert_flight(flight_id: str, flight: FlightCreate):
    stored_flight_model = _get_flight(flight_id)
    if stored_flight_model:
        update_data = flight.dict(exclude_unset=True)
        updated_flight = stored_flight_model.copy(update=update_data)
    else:
        updated_flight = Flight(
            id=flight_id,
            arrival_time=flight.arrival_time,
            departure_time=flight.departure_time
        )

    updated_flight = updated_flight.copy(update={'success': is_successful_flight(updated_flight)})
    _upsert_flight(updated_flight)
    return updated_flight