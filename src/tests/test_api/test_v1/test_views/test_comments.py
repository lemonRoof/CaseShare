#!/usr/bin/python3
"""This module contain test classes for the APIs defined in views.comments"""
import unittest
import requests
from faker import Faker
from models import storage
import jwt
from models.comment import Comment
from models.user import User


class TestComment(unittest.testCase):
    """Test the CRUD Operations on the comments table using APIs defined in views.comment"""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_comments(self):
        pass

    def test_get_one_comment(self):
        pass

    def test_get_comment_by_user(self):
        pass

    def test_create_comment(self):
        pass

    def test_update_comment(self):
        pass

    def test_delete_comment(self):
        pass
