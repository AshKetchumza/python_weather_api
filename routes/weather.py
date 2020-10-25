from flask import request, jsonify
from . import routes
from controllers.weather import construct_weather
import requests
import json

# OpenWeatherMap API key (only stored here for demo purposes)
api_key = "7b0a0bd6f6d765af9fd90160feb7f3ea"

# Main weather endpoint
@routes.route("/weather", methods=['GET'])
def weather():
    try:
        # Get request data
        city = request.args.get('city')
        period = request.args.get('period')
        
        # Validate period as int
        try:
            period = int(period)
        except Exception as err:
            # Respond with 400 for invalid request
            msg = 'Incorrect *period* argument type, only integers are accepted'  
            return jsonify({'msg': msg, 'status': 400}), 400
        
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
        # Respond with 400 for invalid request
        return jsonify({'msg': 'Missing *city* argument', 'status': 400}), 400