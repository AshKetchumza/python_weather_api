from flask import request, jsonify
from . import routes
from controllers.weather import construct_weather
import requests
import json

# OpenWeatherMap API key (only stored here for demo purposes)
api_key = "7b0a0bd6f6d765af9fd90160feb7f3ea"

# Main weather endpoint
@routes.route("/weather", methods=['POST'])
def weather():
    try:
        # Get request data
        city = request.json['city']
        period = request.json['period']        
                
        # Period type validation
        if not isinstance(period, int):
            # Respond with 406 for invalid request
            msg = 'Incorrect *period* type, only integers are accepted'  
            return jsonify({'msg': msg, 'status': 406}), 406
        
        #  Period range validation
        if period > 5 or period <= 0:
            # Respond with 406 for invalid request
            msg = 'Out of range, a min of 1 and a max of 5 days for *period*'   
            return jsonify({'msg': msg, 'status': 406}), 406        

        # City type validation
        if not isinstance(city, str):
            # Respond with 406 for invalid request
            return jsonify({'msg': 'City must be of type String', 'status': 406}), 406
        
        # Make request to 3rd party API for weather data
        url = ("http://api.openweathermap.org/data/2.5/forecast?q=" 
            + city 
            + "&units=metric&cnt=" 
            + str(period*8) 
            + "&appid=" 
            + api_key)
        req = requests.get(url)
        res = json.loads(req.text)
                
        # 3rd part API response validation
        if res['cod'] == '404':
            return jsonify({'msg': res['message'], 'status': 404}), 404

        # Construct weather response data
        data = construct_weather(city, res['list'])
        
        # Respond with 200 status
        return jsonify(data)
    except Exception as err:
        # Handle exception & respond with 400 status
        if len(err.args) == 1:
            msg = 'Missing required {' + err.args[0] + '} request parameter'
        else:
            msg = 'Missing *city* and *period* request parameters'

        return jsonify({'msg': msg, 'status': 400}), 400