from typing import List, Union
from .csv_utils import DATA_FILE_DATE_FORMAT, CSV_FILE_HEADERS, MyCsvIO, csv_date_to_dateime
from .schema import Flight

def flight_to_csv_row(flight: Flight):
    return [
        flight.id, 
        flight.arrival_time.strftime(DATA_FILE_DATE_FORMAT), 
        flight.departure_time.strftime(DATA_FILE_DATE_FORMAT),
        flight.success
    ]

def csv_row_to_flight(csv_row: List):
    return Flight(
                id=csv_row[0],
                arrival_time=csv_date_to_dateime(csv_row[1]),
                departure_time=csv_date_to_dateime(csv_row[2]),
                success=eval(csv_row[3])
            )

def write_flight_list(flight_list):
    with MyCsvIO().get_csv_writer() as spamwriter:
        spamwriter.writerow(dict((heads, heads) for heads in CSV_FILE_HEADERS))
        spamwriter.writerows([{k: v for k, v in zip(CSV_FILE_HEADERS, flight_to_csv_row(flight))} for flight in flight_list])

def get_all_flights() -> List[Flight]:
    with MyCsvIO().get_csv_reader() as spamreader:
        flights = [csv_row_to_flight(csv_row) for csv_row in spamreader]
    return flights

def _get_flight(flight_id: str) -> Union[Flight, None]:
    return next(filter(lambda flight: flight.id == flight_id, get_all_flights()), None)

def _upsert_flight(updated_flight: Flight):
    flights = get_all_flights()
    update_flag = False
    n = []
    for flight in flights:
        if flight.id == updated_flight.id:
            n.append(updated_flight)
            update_flag = True
        else:
            n.append(flight)

    if not update_flag: # we need to insert
        n.append(updated_flight)
    
    write_flight_list(n)

def get_todays_flight_count():
    return len(list(filter(lambda flight: flight.success, get_all_flights())))