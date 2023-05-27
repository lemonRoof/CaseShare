#!/usr/bin/python3
"""Test the status of an API"""
import unittest
import requests

class testStatus(unittest.TestCase):
    """Test the status of an API"""

    def test_status(self):
        """Send a query to status api and check the results"""
        url = 'http://0.0.0.0:5001/our-apis/v1/status'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertDictEqual(data, {'status': 'OK'})
        