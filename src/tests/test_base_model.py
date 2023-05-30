import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock
from models.base_model import BaseModel
import models

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        models.storage_t = "db"

    def test_init_with_kwargs(self):
        kwargs = {
            "id": "123",
            "created_at": "2023-01-01T00:00:00.000",
            "updated_at": "2023-01-02T00:00:00.000",
            "name": "John",
            "email": "john@example.com",
            "password": "secret"
        }
        with patch.object(datetime, "utcnow", return_value=datetime(2023, 1, 3, 0, 0, 0)):
            obj = BaseModel(**kwargs)

        self.assertEqual(obj.id, "123")
        self.assertEqual(obj.created_at, datetime(2023, 1, 1, 0, 0, 0))
        self.assertEqual(obj.updated_at, datetime(2023, 1, 2, 0, 0, 0))
        self.assertEqual(obj.name, "John")
        self.assertEqual(obj.email, "john@example.com")
        self.assertEqual(obj.password, "secret")

    def test_init_without_kwargs(self):
        with patch.object(datetime, "utcnow", return_value=datetime(2023, 1, 3, 0, 0, 0)):
            obj = BaseModel()

        self.assertIsNotNone(obj.id)
        self.assertEqual(obj.created_at, datetime(2023, 1, 3, 0, 0, 0))
        self.assertEqual(obj.updated_at, datetime(2023, 1, 3, 0, 0, 0))

    def test_save(self):
        obj = BaseModel()
        obj.save()
        self.assertTrue(models.storage.new.called)
        self.assertTrue(models.storage.save.called)

    def test_to_dict(self):
        obj = BaseModel(id="123", created_at=datetime(2023, 1, 1, 0, 0, 0), updated_at=datetime(2023, 1, 2, 0, 0, 0))
        obj.name = "John"
        obj.email = "john@example.com"
        obj.password = "secret"

        result = obj.to_dict()

        expected = {
            "id": "123",
            "created_at": "2023-01-01T00:00:00.000",
            "updated_at": "2023-01-02T00:00:00.000",
            "name": "John",
            "email": "john@example.com",
            "__class__": "BaseModel"
        }
        self.assertEqual(result, expected)

    def test_delete(self):
        obj = BaseModel()
        obj.delete()
        self.assertTrue(models.storage.delete.called)

if __name__ == '__main__':
    unittest.main()
