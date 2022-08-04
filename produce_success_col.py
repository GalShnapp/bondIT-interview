import csv
from datetime import datetime

DATA_FILE_DATE_FORMAT = "%H:%M"

with open('flight_clean_copy.csv') as csvfile:
    spamreader = csv.reader(csvfile, quotechar='|')
    headers = next(spamreader, None)
    success_count = 0
    l = []
    for row in spamreader:
        l.append([i for i in row])

l.sort(key=lambda r: datetime.strptime(r[1].strip(), DATA_FILE_DATE_FORMAT))
for row in l:
    s_time = datetime.strptime(row[1].strip(), DATA_FILE_DATE_FORMAT)
    e_time = datetime.strptime(row[2].strip(), DATA_FILE_DATE_FORMAT)
    minutes = ((e_time - s_time).total_seconds()/60)
    success = minutes > 180 and success_count < 20
    if success:
        success_count = success_count + 1
    row[3] = success


with open('flight.csv', 'w') as csvfile:
    data = csv.DictWriter(csvfile, delimiter=',', fieldnames=headers)
    data.writerow(dict((heads, heads) for heads in headers))
    data.writerows([{header: value for header, value in zip(headers, row)} for row in l])

print("done.")
