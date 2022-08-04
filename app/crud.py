import csv
from datetime import datetime
from contextlib import contextmanager
from typing import List
import pandas as pd
from .schema import Flight


DATA_FILE_NAME = 'flight.csv'
DATA_FILE_DATE_FORMAT = ""

def csv_date_to_dateime(csv_date: str):
    return datetime.strptime(csv_date.strip(), "%H:%M")

def csv_row_to_flight(csv_row: List):
    return Flight( 
                id=csv_row[0], 
                arrival_time=csv_date_to_dateime(csv_row[1]), 
                departure_time=csv_date_to_dateime(csv_row[2]),
                success=eval(csv_row[3])
            )

  
class MyCsvIO(object):
    def __init__(self):
        self.file_name = DATA_FILE_NAME
  
    @contextmanager
    def get_csv_reader(self):
        try:
            csvfile = open(self.file_name, 'r')
            spamreader = csv.reader(csvfile, quotechar='|')
            h = next(spamreader, None)
            yield spamreader
        finally:
            csvfile.close()
    
    @contextmanager
    def get_csv_writer(self):
        try:
            csvfile = open(self.file_name, 'w')
            spamreader = csv.reader(csvfile, quotechar='|')
            h = next(spamreader, None)
            yield spamreader
        finally:
            csvfile.close()


def get_flight(flight_id: str):
    flight = []
    with MyCsvIO().get_csv_reader() as spamreader:
        flights = [csv_row_to_flight(csv_row) for csv_row in spamreader]

    return next(filter(lambda flight: flight.id == flight_id, flights), None)
