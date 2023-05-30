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
    
    def test_pep8_conformance_image(self):
        """Test that models/document.py conforms to PEP8."""
        pass

    def test_pep8_conformance_test_document(self):
        """Test that tests/test_models/test_document.py conforms to PEP8."""
        pass
        
    def test_post_module_docstring(self):
        """Test for the image.py module docstring"""
        pass
        
    def test_image_class_docstring(self):
        """Test for the Document class docstring"""
        pass
        
    def test_image_class_docstring(self):
        """Test for the Document class docstring"""
        pass
        
    def test_Image_func_docstrings(self):
        """Test for the presence of docstrings in Image methods"""
        pass    

class TestImage(unittest.TestCase):
    """Test the Image class"""
    def test_is_subclass(self):
        """Test if Image is a subclass of BaseModel"""
        pass

    def test_user_id_attr(self):
        """Test User has attr user_id, and it's an empty string"""
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
