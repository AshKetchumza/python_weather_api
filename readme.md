# Python RESTful weather API

## User story

> As an API user I want to get min, max, average and median temperature and humidity for given city and period of time

## Usability

> You will need to get your own API key to use this, you can get on from https://openweathermap.org/api

## Goals

> Create locally running RESTful web API ✅

> That accepts a request with 'city' and 'period' args ✅

> Fetches weather data for that location and period of time from some public API ✅

> Computes min, max, average and median temperature and humidity for that location and period ✅

> Unit test application ✅

> Render graph from data ✅

## Graph Readability

> Min temp, max temp, and humidity are all shown on the single graph

> The x axis can be read by viewing the number as a time i.e 03 = 03:00 (3am), 12 = 12:00 (12pm), 00 = 00:00 (12am)

> The y axis has a range of 0 to 100, where temperatures are in celcius and humidity is a percentage

> Light blue for humidity, red for max temp and orange for min temp

## Run Locally (Requires Python 3.*)

``` bash
# Install dependencies
$ pip install -r requirements.txt

# Run via flask (http://localhost:5000)
flask run

# Run via script (http://localhost:5000)
python app.py
```

## Endpoints

* GET     /weather
* GET     /

> GET /weather endpoint requires city and period parameters

> period parameter accepts only integers, any values below 1 or over 5 will result in a 5 day query

> Example valid request in browser
``` bash
http://localhost:5000/weather?city=Cape Town&period=1
```

> Example invalid request in browser
``` bash
http://localhost:5000/weather?city=Cape Town&period=1.5
```

## Unit Tests

``` bash
# To run only the tests
python -m unittest discover __unittests__

# To get a coverage report
coverage run -m unittest discover __unittests__/
coverage report -m
```