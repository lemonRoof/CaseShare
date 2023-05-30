#!/usr/bin/python3
"""
Contains the TesstCommentDocs classes
"""

import unittest

class TestCommentDocs(unittest.TestCase):
    """Tests to check the documentation and style of Comment class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        pass
        

    def test_pep8_conformance_comment(self):
        """Test that models/comment.py conforms to PEP8."""
        pass
        
    def test_pep8_conformance_test_comment(self):
        """Test that tests/test_models/test_comment.py conforms to PEP8."""
        pass
        
    def test_comment_module_docstring(self):
        """Test for the comment.py module docstring"""
        pass
        
    def test_comment_class_docstring(self):
        """Test for the Comment class docstring"""
        pass
        
    def test_comment_func_docstrings(self):
        """Test for the presence of docstrings in Comment methods"""
        pass
            
class TestComment(unittest.TestCase):
    """Test the Comment class"""
    def test_is_subclass(self):
        """Test if Comment is a subclass of BaseModel"""
        pass

    def test_post_id_attr(self):
        """Test Comment has attr post_id, and it's an empty string"""
        pass

    def test_user_id_attr(self):
        """Test Comment has attr user_id, and it's an empty string"""
        pass

    def test_text_attr(self):
        """Test Comment has attr text, and it's an empty string"""
        pass

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        pass

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        pass

    def test_str(self):
        """test that the str method has the correct output"""
        pass
