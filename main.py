import csv
from datetime import datetime

with open('flight_clean_copy.csv') as csvfile:
    spamreader = csv.reader(csvfile, quotechar='|')
    h = next(spamreader, None)
    sec_count = 0
    l = []
    for row in spamreader:
        l.append([i for i in row])

    l.sort(key=lambda r: datetime.strptime(r[1].strip(), "%H:%M"))
    for row in l:
        s_time = datetime.strptime(row[1].strip(), "%H:%M")
        e_time = datetime.strptime(row[2].strip(), "%H:%M")
        minutes = ((e_time - s_time).total_seconds()/60)
        success = minutes > 180 and sec_count < 20
        if success == True:
            sec_count = sec_count + 1
        row[3] = success


with open('flight.csv', 'w') as csvfile:
    data = csv.DictWriter(csvfile, delimiter=',', fieldnames=h)
    data.writerow(dict((heads, heads) for heads in h))
    data.writerows([{k: v for k, v in zip(h, row)} for row in l])

print("done.")
