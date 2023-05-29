#!/usr/bin/python3
"""Test if the decorator function works as intended"""
import unittest
from faker import Faker
import jwt
from flask import Flask
from api.v1.views.decorators import token_required
from datetime import datetime, timedelta
from os import getenv

app = Flask(__name__)

@app.route('/')
@token_required
def who_entered(email):
    return email


class TestDecorators(unittest.TestCase):
    """Test if decorators work as anticipated"""

    def setUp(self):
        """Set the test client"""
        self.app = app.test_client()

    def test_decorator_with_no_token_request(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 403)
        self.assertDictEqual(response.get_json(), {'error': 'invalid token'})

    def test_decorator_with_a_token(self):
        fake = Faker()
        SECRET_TOKEN = getenv('SECRET_KEY')
        email = fake.email()
        token = jwt.encode({'email': email, 'exp':datetime.now() + timedelta(minutes=5)}, SECRET_TOKEN)
        response = self.app.get('/', headers={'x-token': token})
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    app.run()