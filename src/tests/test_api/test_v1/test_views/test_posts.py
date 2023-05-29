#!/usr/bin/python3
"""This module contain test classes for the APIs defined in views.posts"""
import unittest
import requests
from faker import Faker
from models import storage
import jwt
from api.v1.views.decorator import token_required
from models.post import Post
from models.user import User
from os import getenv


class TestPost(unittest.testCase):
    """Test the CRUD Operations on the posts table using APIs defined in views.post"""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        fake = Faker()
        self.user = User(email=fake.email(), password=fake.password(), first_name=fake.first_name(), last_name=fake.last_name(),
                         country=fake.country(), title=fake.sentence(), phone=fake.basic_phone_number(), age=12)
        self.user.save()
        self.token = jwt.encode({'email': self.user.email, 'exp': datetime.now() + timedelta(seconds=30)}, getenv('SECRET_KEY'))
        self.post(user_id = self.user.id, title = fake.sentence(), content = fake.sentences(nb=3))
        self.post.save()

    def tearDown(self):
        pass

    def test_get_posts(self):
        url = 'http://0.0.0.0:5001/our-apis/posts'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertEqual(len(response.json()), 1)

    def test_get_one_post(self):
        url = 'http://00.0.0:5001/our'

    def test_get_post_by_user(self):
        pass

    def test_create_post(self):
        pass

    def test_update_post(self):
        pass

    def test_delete_post(self):
        pass