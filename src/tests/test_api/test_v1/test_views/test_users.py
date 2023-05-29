#!/usr/bin/python3
"""Test APIs to do CRUD operations on table user"""
import unittest
import json
import jwt
from werkzeug.security import check_password_hash
import requests
from models import storage
from faker import Faker
from models.user import User
from datetime import timedelta, datetime
from os import getenv

class testUser(unittest.TestCase):
    """Test CRUD operations on users table, including log in and log out"""

    @classmethod
    def setUpClass(cls):
        """Delete all the data in the table users"""
        users = storage.all(User)
        [user.delete() for user in users]

    @classmethod
    def tearDownClass(cls):
        """Delete all the data in the table users"""
        users = storage.all(User)
        [user.delete() for user in users]

    def setUp(self):
        """Create a user object to play with"""
        fake = Faker()
        self.user = User(email=fake.email(), password=fake.password(), first_name=fake.first_name(), last_name=fake.last_name(),
                         country=fake.country(), title=fake.sentence(), phone=fake.basic_phone_number(), age=12)
        self.user.save()
        self.token = jwt.encode({'email': self.user.email, 'exp': datetime.now() + timedelta(seconds=30)}, getenv('SECRET_KEY'))

    def tearDown(self):
        """Remove the created object"""
        self.user.delete()

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
            'dob': 23,
            'phone': '07897817878'
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        self.assertEqual(response.status_code, 201)
        user_id = response.json()
        storage.reload()
        user = storage.get(User, user_id)
        self.assertEqual(user.email, data['email'])


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

    def test_get_users(self):
        """Test if we can get the number of all users in the database"""
        url = 'http://0.0.0.0:5001/our-apis/v1/users'
        headers = {'x-token': self.token}
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertIsInstance(response.json(), list)

    def test_get_myself(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/users/myself'
        headers = {'x-token': self.token}
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertNotIn('password', response.json().keys())
        self.assertEqual(response.json().get('id'), self.user.id)

    
    def test_get_user_with_valid_id(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/users/{}'.format(self.user.id)
        headers = {'x-token': self.token}
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertNotIn('password', response.json().keys())
        self.assertEqual(response.json().get('id'), self.user.id)

    
    def test_get_user_with_invalid_id(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/users/invalid'
        headers = {'x-token': self.token}
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 404)
        self.assertIsInstance(response.json(), dict)
        self.assertIn('error', response.json().keys())
        self.assertEqual(response.json().get('error'), 'Not Found')

    def test_update_with_valid_data(self):
        self.assertEqual(self.user.age, 12)
        url = 'http://0.0.0.0:5001/our-apis/v1/users/myself'
        headers = {'x-token': self.token, 'Content-Type': 'application/json'}
        data = {
            'title': "I have a different title",
            'email': "something@abc.com"
        }
        response = requests.put(url, data=json.dumps(data), headers=headers)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, dict)
        self.assertNotIn('password', result.keys())
        self.assertEqual(result.get('id'), self.user.id)
        self.assertNotEqual(result.get('email'), self.user.email)
        self.assertNotEqual(result.get('title'), self.user.title)
        self.assertEqual(result.get('phone'), self.user.phone)

    def test_update_with_invalid_json(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/users/myself'
        headers = {'x-token': self.token, 'Content-Type': 'application/json'}
        data = {
            'title': "I have a different title",
            'email': "something@abc.com"
        }
        response = requests.put(url, data=data, headers=headers)
        result = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertIn('Not a JSON', result.values())

    def test_change_password_with_valid_data(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/users/myself/change_password'
        headers = {'x-token': self.token, 'Content-Type': 'application/json'}
        data = {
            'old_password': self.user.password,
            'new_password': "ThisisnewPassword"
        }
        response = requests.put(url, data=json.dumps(data), headers=headers)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(result, {})

    def test_change_password_with_invalid_old_password(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/users/myself/change_password'
        headers = {'x-token': self.token, 'Content-Type': 'application/json'}
        data = {
            'old_password': "Invalid password",
            'new_password': "ThisisnewPassword"
        }
        response = requests.put(url, data=json.dumps(data), headers=headers)
        result = response.json()
        self.assertEqual(response.status_code, 403)
        self.assertIn('Invalid Password', result.values())

    def test_change_password_with_invalid_json(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/users/myself/change_password'
        headers = {'x-token': self.token, 'Content-Type': 'application/json'}
        data = {
            'old_password': self.user.password,
            'new_password': "ThisisnewPassword"
        }
        response = requests.put(url, data=data, headers=headers)
        result = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertIn('Not a JSON', result.values())

    def test_reset_password_with_valid_data(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/users/myself/reset_password'
        headers = {'x-token': self.token, 'Content-Type': 'application/json'}
        data = {
            'new_password': "ThisisnewPassword"
        }
        response = requests.put(url, data=json.dumps(data), headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_reset_password_with_invalid_json(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/users/myself/reset_password'
        headers = {'x-token': self.token, 'Content-Type': 'application/json'}
        data = {
            'new_password': "ThisisnewPassword"
        }
        response = requests.put(url, data=data, headers=headers)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Not a JSON', response.json().values())

    @unittest.expectedFailure
    def test_delete(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/users/myself'
        headers = {'x-token': self.token}
        response = requests.delete(url, headers=headers)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(response.json()), 0)
        self.assertIsNone(storage.get(User, self.user.id))