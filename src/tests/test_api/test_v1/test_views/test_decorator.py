#!/usr/bin/python3
"""This directory tests decorators defined in the views/decorators.py file"""
import unittest
from api.v1.views.decorators import token_required
from faker import Faker
import requests
import json

@unittest.skip('Let go for now')
class TestDecorator(unittest.TestCase):
    """Test if decorators work as we expect them to"""
    
    @classmethod
    def setUpClass(cls):

        fake = Faker()
        """Create an object to test with"""
        obj = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'dob': '20010402',
            'title': 'Radiographer at XYZ hospital',
            'password': fake.password(),
            'country': fake.country(),
            'phone': fake.basic_phone_number()
        }
        headers = {'Content-Type': 'application/json'}
        url = 'http://0.0.0.0:5001/our-apis/v1/register'
        resp = requests.post(url, data=json.dumps(obj), headers=headers)
        if not resp.OK:
            return