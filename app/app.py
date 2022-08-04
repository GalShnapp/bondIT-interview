from fastapi import FastAPI, HTTPException
from .crud import get_flight

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/flight_info/{flight_id}")
async def get_flight_info(flight_id):
    flight = get_flight(flight_id)
    if flight is None:
        raise HTTPException(status_code=404, detail=f"flight {flight_id} not found")
    return flight

