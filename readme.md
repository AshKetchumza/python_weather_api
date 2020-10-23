# Python RESTful weather API

## User story

> As an API user I want to get min, max, average and median temperature and humidity for given city and period of time

## Goals

> Create locally running RESTful web API ✅

> That accepts a request with 'city' and 'period' args ✅

> Fetches weather data for that location and period of time from some public API ✅

> Computes min, max, average and median temperature and humidity for that location and period ✅

> Unit test application ✅

## Extra Goals

> Provide a view which renders a bar chart for the requested data ✅ (API responds with image based graph in response data instead of rendering a view)

> Deploy it somewhere ✅ Deployed to AWS EC2 - use http://13.244.62.50:5000/ as URL

## Graph Readability

> Min temp, max temp, and humidity are all shown on the single graph

> The x axis can be read by viewing the number as a time i.e 03 = 03:00 (3am), 12 = 12:00 (12pm), 00 = 00:00 (12am)

> The y axis has a range of 0 to 100, where temperatures are in celcius and humidity is a percentage

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

* POST    /weather
* GET     /

> POST method requires city and period parameters

> city parameter accepts only strings

> period parameter accepts values from 1 to 5, accepts only integers

> Example valid request body
``` bash
{
    "city": "Cape Town",
    "period": 5
}
```

> Example invalid request body
``` bash
{
    "city": ["Cape Town"],
    "period": 5.0
}
```

## Unit Tests

``` bash
# To run only the tests
python -m unittest discover __unittests__

# To get a coverage report
coverage run -m unittest discover __unittests__/
coverage report -m
```