# bondIT-interview

This repo is my response to bondIT's two part interview exercise.

## Part one - Produce a ‘success’ column for the data given in flight_clean_copy.csv
The code that handles this is a script called ```produce_success_col.py ```. To run it, just run
```sh
JohnDoe@Host:~/bondIT-interview $ python produce_success_col.py
done.
```
The above command will produce a file called```flight.csv``` which will have the same data as the original file, only it will also have a success column and it's rows will be sorted by arrival time. a filght is a success if its longer than 3 hours and there aren't  more than 20 successful flights in DB.

> **_NOTE:_**  It is useful to use this script to restart the DB to a clean slate for part II

## Part two - get and upsert flights restAPI
I've created an api using fastAPI. This api is presistent, and uses ```flight.csv``` as if it was a database. To run the server:
```bash
JohnDoe@Host:~/bondIT-interview $ pip install requirements.txt
JohnDoe@Host:~/bondIT-interview $ uvicorn app.app:app --reload
INFO:     Will watch for changes in these directories: ['~/bondIT-interview']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [64981] using statreload
INFO:     Started server process [64983]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
Once the server is up, you can use the native graphical user interface in: http://127.0.0.1:8000/docs#/
where you can play around with the API, and make request to the server.
<br>
Alternatively, you may use the following formats to send requests to the api:
##### upsert
```sh
JohnDoe@Host:~/bondIT-interview $ curl -X 'PUT' \
  'http://127.0.0.1:8000/flights/G884' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": "G887",
  "arrival_time": "12:08",
  "departure_time": "23:08"
}'
```

##### get
```sh
JohnDoe@Host:~/bondIT-interview $ curl -X 'GET' \
  'http://127.0.0.1:8000/flights/G889' \
  -H 'accept: application/json'
```