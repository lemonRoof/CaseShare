#!/usr/bin/python3
"""This module contain test classes for the APIs defined in views.comments"""
import unittest
import requests
from faker import Faker
from models import storage
import jwt
from models.comment import Comment
from models.user import User
from models.post import Post
from os import getenv
import json
from datetime import datetime, timedelta


class TestComment(unittest.TestCase):
    """Test the CRUD Operations on the comments table using APIs defined in views.comment"""

    @classmethod
    def setUpClass(cls):
        [post.delete() for post in storage.all(Post)]
        [user.delete() for user in storage.all(User)]
        [comment.delete() for comment in storage.all(Comment)]
        storage.save()

    def setUp(self):
        fake = Faker()
        self.user = User(email=fake.email(), password=fake.password(), first_name=fake.first_name(), 
                         last_name=fake.last_name(), country=fake.country(), title=fake.sentence(),
                         phone=fake.basic_phone_number(), age=12)
        self.user.save()
        self.token = jwt.encode({'email': self.user.email, 'exp': datetime.now() + timedelta(seconds=60)}, getenv('SECRET_KEY'))
        self.post = Post(user_id=self.user.id, title=fake.sentence(), content=fake.sentence())
        self.post.save()
        self.comment = Comment(user_id=self.user.id, post_id=self.post.id, content=fake.sentence())
        self.comment.save()

    def tearDown(self):
        storage.delete(self.user)
        storage.delete(self.post)
        storage.delete(self.comment)
        storage.save()

    def test_get_comments(self):
        url = "http://0.0.0.0:5001/our-apis/v1/posts/{}/comments".format(self.post.id)
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertNotEqual(len(response.json()), 0)

    def test_get_one_comment(self):
        url = "http://0.0.0.0:5001/our-apis/v1/comments/{}".format(self.comment.id)
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertNotEqual(len(response.json()), 0)
        comment = response.json()
        self.assertEqual(comment['id'], self.comment.id)

    @unittest.skip('No implementation')
    def test_get_comments_by_user(self):
        url = "http://0.0.0.0:5001/our-apis/v1/users/{}/comments".format(self.user.id)
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertNotEqual(len(response.json(), 0))

    def test_create_comment(self):
        url = "http://0.0.0.0:5001/our-apis/v1/posts/{}/comments/".format(self.post.id)
        data = {
            'user_id': self.user.id,
            'post_id': self.post.id,
            'content': "This is a new comment"
        }
        headers = {
            'Content-Type': 'application/json',
            'x-token': self.token
        }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.json(), dict)
        self.assertNotEqual(len(response.json()), 0)
        comment = response.json()
        self.assertEqual(comment['content'], data['content'])

    def test_update_comment(self):
        url = "http://0.0.0.0:5001/our-apis/v1/comments/{}".format(self.comment.id)
        data = {
            'content': "This is a new comment"
        }
        headers = {
            'Content-Type': 'application/json',
            'x-token': self.token
        }
        response = requests.put(url, data=json.dumps(data), headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertNotEqual(len(response.json()), 0)
        comment = response.json()
        self.assertEqual(comment['content'], data['content'])


    def test_delete_comment(self):
        new_comment = Comment(user_id=self.user.id, post_id=self.post.id, content="Here I am")
        new_comment.save()
        self.assertEqual(storage.get(Comment, new_comment.id).id, new_comment.id)
        url = "http://0.0.0.0:5001/our-apis/v1/comments/{}".format(new_comment.id)
   
        headers = {
            'x-token': self.token
        }
        response = requests.delete(url, headers=headers)
        self.assertEqual(response.status_code, 204)