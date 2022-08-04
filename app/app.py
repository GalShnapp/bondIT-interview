from fastapi import FastAPI
from .crud import get_flight

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/flight_info/{flight_id}")
async def get_flight_info(flight_id):
    return get_flight(flight_id)

