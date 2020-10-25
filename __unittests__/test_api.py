import os
import unittest
import json

from app import app

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
        resp = self.app.get('/weather?city=Cape Town&period=1')
        self.assertEqual(resp.status_code, 200)

    # Test weather 400 invalid period type
    def test_weather_400_invalid_period(self):
        print("----".join((" ","Test weather 400 invalid period type"," ")))
        resp = self.app.get('/weather?city=Cape Town&period=1.5')
        self.assertEqual(resp.status_code, 400)

    # Test weather 400 missing city arg
    def test_weather_400_missing_city(self):
        print("----".join((" ","Test weather 400 missing city arg"," ")))
        resp = self.app.get('/weather?period=1')
        self.assertEqual(resp.status_code, 400)

    # Test weather 404
    def test_weather_404(self):
        print("----".join((" ","Test weather 404 city not found"," ")))
        resp = self.app.get('/weather?city=faketown&period=1')
        self.assertEqual(resp.status_code, 404)   