import unittest
from models.document import Document
import models

class TestDocument(unittest.TestCase):
    def setUp(self):
        models.storage_t = "db"

    def test_init_with_kwargs(self):
        kwargs = {
            "id": "123",
            "created_at": "2023-01-01T00:00:00.000",
            "updated_at": "2023-01-02T00:00:00.000",
            "filename": "document.txt",
            "post_id": 1
        }
        obj = Document(**kwargs)

        self.assertEqual(obj.id, "123")
        self.assertEqual(obj.created_at, datetime(2023, 1, 1, 0, 0, 0))
        self.assertEqual(obj.updated_at, datetime(2023, 1, 2, 0, 0, 0))
        self.assertEqual(obj.filename, "document.txt")
        self.assertEqual(obj.post_id, 1)

    def test_init_without_kwargs(self):
        obj = Document()

        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)
        self.assertEqual(obj.filename, "")
        self.assertEqual(obj.post_id, "")

if __name__ == '__main__':
    unittest.main()
