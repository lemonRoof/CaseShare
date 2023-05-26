#!/usr/bin/python3
"""Test if CRUD operations with a mysql database are working"""

import unittest
from models.engine.db_storage import DBStorage
storage = DBStorage()


class TestEngine(unittest.TestCase):
    """Create test cases for the database engine"""

    def test_all_with_class(self):
        pass

    def test_all_with_class_name(self):
        pass

    def test_all_with_invalid_class(self):
        pass

    def test_all_with_none(self):
        pass

    def test_save(self):
        pass
    
    def test_delete_with_obj(self):
        pass

    def test_delete_with_invalid_object(self):
        pass

    def test_new(self):
        pass

    def test_reload(self):
        pass

    def test_get_with_valid_class_and_id(self):
        pass

    def test_get_with_invalid_class(self):
        pass

    def test_get_with_invalid_object(self):
        pass

    def test_close(self):
        pass

    def test_count_with_valid_class(self):
        pass

    def test_count_with_invalid_class(self):
        pass