#!/usr/bin/python3
"""
Contains the TestUserDocs classes
"""

import unittest

class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style or User class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        pass

    def test_pep8_conformance_user(self):
        """Test that models/user.py confroms to PEP8."""
        pass

    def test_pep8_conformance_test_user(self):
        """Test that test/test_models/test)_user.py conforms to PEP8."""
        pass

    def test_user_module_docstring(self):
        """Test for the user.py module docstring"""
        pass

    def test_user_class_docstring(self):
        """Test for the  Post class docstring"""
        pass
    
    def test_user_func_docstrings(self):
        """Test for the presence of docstring in User methods"""
        pass

class TestUser(unittest.TestCase):
    """Test the User class"""
    def test_is_subclass(self):
        """Test that User is a subclass of BaseModel"""
        pass

    def test_email_attr(self):
        """Test that User has attr email, and it's an email, and it'sv an empty string"""
        pass

    def test_password_attr(self):
        """Test the User has attr password, and it's an epty string"""
        pass

    def test_first_name_attr(self):
        """Test that User has attr first_name, and it's an empty string"""
        pass

    def test_last_name_attr(self):
        """Test that User has attr last_name, and it's an empty string"""
        pass

    def test_to_dict_creates_dict(self):
        """test to_dict merhod creates a dictionary with proper attrs"""
        pass

    def test_to_dict_value(self):
        """test that values in dict returned from to_dict are correct"""
        pass

    def test_str(self):
        """test that the str method has the correct output"""
        pass
