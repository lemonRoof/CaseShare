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

    def test_pep8_conformance_video(self):
        """Test that models/video.py conforms to PEP8."""
        pass
        
    def test_pep8_conformance_test_video(self):
        """Test that tests/test_models/test_image.py conforms to PEP8."""
        pass
        
    def test_post_module_docstring(self):
        """Test for the video.py module docstring"""
        pass
        
    def test_video_class_docstring(self):
        """Test for the video class docstring"""
        pass
        
    def test_image_class_docstring(self):
        """Test for the Video class docstring"""
        pass
        
    def test_Video_func_docstrings(self):
        """Test for the presence of docstrings in Video methods"""
        pass

class TestVideo(unittest.TestCase):
    """Test the Video class"""
    def test_is_subclass(self):
        """Test if Video is a subclass of BaseModel"""
        pass

    def test_user_id_attr(self):
        """Test Video has attr user_id, and it's an empty string"""
        pass

    def test_text_id_attr(self):
        """Test video has attr text, and it's an empty string"""
        pass

    def test_comment_id_attr(self):
        """Test post has attr comment, and it's an empty string"""
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
