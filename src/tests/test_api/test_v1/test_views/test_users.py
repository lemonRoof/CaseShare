#!/usr/bin/python3
"""Test APIs to do CRUD operations on table user"""
import unittest
import json
import requests
from models import storage
from models.models import User

class testUser(unittest.TestCase):
    """Test CRUD operations on users table, including log in and log out"""

    @classmethod
    def setUpClass(cls):
        """Delete all the data in the table users"""
        users = storage.all(User)
        [user.delete() for user in users]

    def test_create_user_with_valid_data(self):
        """Test if the user can sign up with valid data"""
        url = 'http://0.0.0.0:5001/our-apis/v1/register'
        data = {
            'email': 'muhi@gmail.com',
            'password': 'abcdefgh',
            'first_name': 'Muhire',
            'last_name': 'Lionel',
            'title': 'ALX SE Student C13, Medical Imaging Graduate',
            'country': 'Rwanda',
            'dob': '19930623',
            'phone': '07897817878'
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        self.assertEqual(response.status_code, 201)
        user = storage.get(User, data['email'])
        self.assertEqual(user.first_name, data['first_name'])
        self.assertEqual(user.last_name, data['last_name'])


    def test_create_with_invalid_json(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/register'
        data = None
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=data, headers=headers)
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(response.json(), {'error': 'Not a JSON'})

    def test_create_user_with_missing_data(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/register'
        data = {
            'password': "This will fail"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'Missing some data'})


    def test_login_with_valid_data(self):
        """Test if a user with valid credentials can log in"""
        url = 'http://0.0.0.0:5001/our-apis/v1/login'
        data = {
            'email': 'muhi@gmail.com',
            'password': 'abcdefgh'
        }
        headers = {'Content-Type': 'application/json'}
        resp = requests.post(url, data=json.dumps(data), headers=headers)
        self.assertIn('token', resp.json())
        self.assertEqual(resp.status_code, 200)

    def test_login_with_invalid_json(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/login'
        data = None
        headers = {'Content-Type': 'application/json'}
        resp = requests.post(url, data=data, headers=headers)
        self.assertEqual(resp.status_code, 400)
        self.assertDictEqual(resp.json(), {'error': 'Not a JSON'})

    def test_login_with_invalid_password(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/login'
        data = {
            'email': 'muhi@gmail.com',
            'password': 'This is wrong'
        }
        headers = {'Content-Type': 'application/json'}
        resp = requests.post(url, data=json.dumps(data), headers=headers)
        self.assertEqual(resp.status_code, 400)
        self.assertDictEqual(resp.json(), {'error': 'Invalid password'})

    def test_login_with_invalid_email(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/login'
        data = {
            'email': "Bora Hangrobe",
            'password': 'Who cares?'
        }
        headers = {'Content-Type': 'application/json'}
        resp = requests.post(url, data=json.dumps(data), headers=headers)
        self.assertEqual(resp.status_code, 400)
        self.assertDictEqual(resp.json(), {'error': 'email doesnot exist'})