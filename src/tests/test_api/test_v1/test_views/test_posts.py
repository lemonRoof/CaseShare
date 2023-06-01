#!/usr/bin/python3
"""This module contain test classes for the APIs defined in views.posts"""
import json
import unittest
import requests
from faker import Faker
from models import storage
import jwt
from models.post import Post
from models.user import User
from os import getenv
from datetime import datetime, timedelta


class TestPost(unittest.TestCase):
    """Test the CRUD Operations on the posts table using APIs defined in views.post"""

    @classmethod
    def setUpClass(cls):
        [post.delete() for post in storage.all(Post)]
        [user.delete() for user in storage.all(User)]

    def setUp(self):
        fake = Faker()
        self.user = User(email=fake.email(), password=fake.password(), first_name=fake.first_name(), 
                         last_name=fake.last_name(), country=fake.country(), title=fake.sentence(),
                         phone=fake.basic_phone_number(), age=12)
        self.user.save()
        self.token = jwt.encode({'email': self.user.email, 'exp': datetime.now() + timedelta(seconds=30)}, getenv('SECRET_KEY'))
        self.post = Post(user_id = self.user.id, title = fake.sentence(), content = fake.sentence())
        self.post.save()

    def tearDown(self):
        self.user.delete()
        self.post.delete()

    def test_get_posts(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/posts'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertEqual(len(response.json()), 1)

    def test_get_one_post(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/posts/{}'.format(self.post.id)
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertEqual(response.json()['id'], self.post.id)


    def test_get_post_by_user(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/users/{}/posts'.format(self.user.id)
        headers = {'x-token': self.token}
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0].get('id'), self.post.id)


    def test_create_post(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/posts'
        headers = {'Content-Type': 'application/json', 'x-token': self.token}
        data = {
            'user_id': self.user.id,
            'title': "A new Monomer",
            'content': "We discovered something strange. We discovered nothing."
        }
        response = requests.post(url, data = json.dumps(data), headers=headers)
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.json(), dict)
        self.assertEqual(response.json()['title'], data['title'])


    def test_update_post(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/posts/{}'.format(self.post.id)
        data = {
            'title': "A new Title"
        }
        headers = {'Content-Type': 'application/json', 'x-token': self.token}
        response = requests.put(url, data=json.dumps(data), headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertEqual(response.json()['title'], data['title'])


    def test_delete_post(self):
        url = 'http://0.0.0.0:5001/our-apis/v1/posts/{}'.format(self.post.id)
        headers = {'x-token': self.token}
        response = requests.delete(url, headers=headers)
        self.assertEqual(response.status_code, 204)