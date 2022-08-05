import csv
from datetime import datetime
from contextlib import contextmanager


DATA_FILE_NAME = 'flight.csv'
DATA_FILE_DATE_FORMAT = "%H:%M"
CSV_FILE_HEADERS = ["flight ID", "Arrival", "Departure","success"]

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
            spamwriter = csv.DictWriter(csvfile, delimiter=',', fieldnames=CSV_FILE_HEADERS)
            yield spamwriter
        finally:
            csvfile.close()


def csv_date_to_dateime(csv_date: str):
    return datetime.strptime(csv_date.strip(), DATA_FILE_DATE_FORMAT)

