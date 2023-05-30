#!/usr/bin/python3
"""
Contains the TestLikeDocs classes
"""

import unittest

class TestLikeDocs(unittest.TestCase):
    """Tests to check the documentation and style of Like class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""

    def test_pep8_conformance_like(self):
        """Test that models/like.py conforms to PEP8."""

    def test_pep8_conformance_like(self):
        """Test that tests/test_models/test_like.py conforms to PEP8."""

    def test_like_module_docstring(self):
        """Test for the like.py module docstring"""

    def test_like_class_docstring(self):
        """Test for the Like class docstring"""

    def test_like_func_docstring(self):
        """Test for the presence of docsttring in Like State methods"""

class TestLike(unittest.TestCase):
    """Test the like class"""
    def test_is_subclass(self):
        """Test that Like is a subclass of BaseModel"""
        

    def test_name_attr(self):
        """Test that State has attribute name, and it's as an empty string"""

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""

    def test_str(self):
        """test that the str method has the correct output"""
