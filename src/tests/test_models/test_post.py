#!/usr/bin/python3
"""
Contains the TestReviewDocs classes
"""

import unittest

class TestPostDocs(unittest.TestCase):
    """Tests to check the documentation and style of Comment class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        pass

    def test_pep8_conformance_post(self):
        """Test that models/post.py conforms to PEP8."""
        pass
        
    def test_pep8_conformance_test_post(self):
        """Test that tests/test_models/test_post.py conforms to PEP8."""
        pass
        
    def test_post_module_docstring(self):
        """Test for the post.py module docstring"""
        pass
        
    def test_post_class_docstring(self):
        """Test for the Post class docstring"""
        pass
        
    def test_post_class_docstring(self):
        """Test for the Post class docstring"""
        pass
        
    def test_post_func_docstrings(self):
        """Test for the presence of docstrings in Post methods"""
        pass

class TestPost(unittest.TestCase):
    """Test the Post class"""
    def test_is_subclass(self):
        """Test if Post is a subclass of BaseModel"""
        pass

    def test_image_id_attr(self):
        """Test post has attr image_id, and it's an empty string"""
        pass

    def test_user_id_attr(self):
        """Test Post has attr user_id, and it's an empty string"""
        pass

    def test_text_id_attr(self):
        """Test Post has attr text, and it's an empty string"""
        pass

    def test_comment_id_attr(self):
        """Test post has attr comment, and it's an empty string"""
        pass

    def test_video_id_attr(self):
        """Test Review has attr video, and it's an empty string"""
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
