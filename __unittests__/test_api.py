import os
import unittest
import json

from app import app

# Test request data
headers = {"content-type": "application/json"}          
data_json = json.dumps({'city': 'Cape Town', 'period': 1}) 

class UnitTests(unittest.TestCase):

# Setup and teardown
 
    # Executed prior to each test to setup DB
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False        
        self.app = app.test_client()
       
        self.assertEqual(app.debug, False)
 
    # Executed after each test
    def tearDown(self):
        pass 

# Unit Tests 
    
    # Test index
    def test_index(self):
        print("----".join((" ","Test index"," ")))  
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)

    # Test weather 200
    def test_weather_200(self):
        print("----".join((" ","Test weather 200 success"," ")))
        data_json = json.dumps({'city': 'Cape Town', 'period': 1})
        resp = self.app.post('/weather', data=data_json, headers=headers)
        self.assertEqual(resp.status_code, 200)

    # Test weather 406 period out of range
    def test_weather_406_range(self):
        print("----".join((" ","Test weather 406 period out of range"," ")))
        data_json = json.dumps({'city': 'Cape Town', 'period': 6})
        resp = self.app.post('/weather', data=data_json, headers=headers)
        self.assertEqual(resp.status_code, 406)

    # Test weather 406 period of incorrect type
    def test_weather_406_period_type(self):
        print("----".join((" ","Test weather 406 period of incorrect type"," ")))
        data_json = json.dumps({'city': 'Cape Town', 'period': 2.5})
        resp = self.app.post('/weather', data=data_json, headers=headers)
        self.assertEqual(resp.status_code, 406)

    # Test weather 406 city of incorrect type
    def test_weather_406_city_type(self):
        print("----".join((" ","Test weather 406 city of incorrect type"," ")))
        data_json = json.dumps({'city': 1, 'period': 1})
        resp = self.app.post('/weather', data=data_json, headers=headers)
        self.assertEqual(resp.status_code, 406)

    # Test weather 404 city not found
    def test_weather_404(self):
        print("----".join((" ","Test weather 404 city not found"," ")))
        data_json = json.dumps({'city': 'null', 'period': 1})
        resp = self.app.post('/weather', data=data_json, headers=headers)
        self.assertEqual(resp.status_code, 404)

    # Test weather 400 missing period param
    def test_weather_400_period(self):
        print("----".join((" ","Test weather 400 missing period param"," ")))
        data_json = json.dumps({'city': 'Cape Town'})
        resp = self.app.post('/weather', data=data_json, headers=headers)
        self.assertEqual(resp.status_code, 400)

    # Test weather 400 missing city param
    def test_weather_400_city(self):
        print("----".join((" ","Test weather 400 missing city param"," ")))
        data_json = json.dumps({'period': 1})
        resp = self.app.post('/weather', data=data_json, headers=headers)
        self.assertEqual(resp.status_code, 400)

    # Test weather 400 missing all params
    def test_weather_400_all(self):
        print("----".join((" ","Test weather 400 missing all params"," ")))        
        resp = self.app.post('/weather', headers=headers)
        self.assertEqual(resp.status_code, 400)