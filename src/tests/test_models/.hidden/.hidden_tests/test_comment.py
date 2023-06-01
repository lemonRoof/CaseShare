import unittest
from datetime import datetime
from unittest.mock import patch
from models.comment import Comment
import models

class TestComment(unittest.TestCase):
    def setUp(self):
        models.storage_t = "db"

    def test_init_with_kwargs(self):
        kwargs = {
            "id": "123",
            "created_at": "2023-01-01T00:00:00.000",
            "updated_at": "2023-01-02T00:00:00.000",
            "content": "This is a comment",
            "timestamp": "2023-01-03T00:00:00.000",
            "user_id": 1,
            "post_id": 2
        }
        with patch.object(Comment, "__init__", BaseModel.__init__):
            obj = Comment(**kwargs)

        self.assertEqual(obj.id, "123")
        self.assertEqual(obj.created_at, datetime(2023, 1, 1, 0, 0, 0))
        self.assertEqual(obj.updated_at, datetime(2023, 1, 2, 0, 0, 0))
        self.assertEqual(obj.content, "This is a comment")
        self.assertEqual(obj.timestamp, datetime(2023, 1, 3, 0, 0, 0))
        self.assertEqual(obj.user_id, 1)
        self.assertEqual(obj.post_id, 2)

    def test_init_without_kwargs(self):
        with patch.object(Comment, "__init__", BaseModel.__init__):
            obj = Comment()

        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)
        self.assertEqual(obj.content, "")
        self.assertEqual(obj.timestamp, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.post_id, "")

if __name__ == '__main__':
    unittest.main()
