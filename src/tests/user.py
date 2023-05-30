import unittest
from models.user import User
import models

class TestUser(unittest.TestCase):
    def setUp(self):
        models.storage_t = "db"

    def test_init_with_kwargs(self):
        kwargs = {
            "id": "123",
            "created_at": "2023-01-01T00:00:00.000",
            "updated_at": "2023-01-02T00:00:00.000",
            "email": "test@example.com",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe"
        }
        obj = User(**kwargs)

        self.assertEqual(obj.id, "123")
        self.assertEqual(obj.created_at, datetime(2023, 1, 1, 0, 0, 0))
        self.assertEqual(obj.updated_at, datetime(2023, 1, 2, 0, 0, 0))
        self.assertEqual(obj.email, "test@example.com")
        self.assertEqual(obj.password, md5("password123".encode()).hexdigest())
        self.assertEqual(obj.first_name, "John")
        self.assertEqual(obj.last_name, "Doe")

    def test_init_without_kwargs(self):
        obj = User()

        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)
        self.assertEqual(obj.email, "")
        self.assertEqual(obj.password, "")
        self.assertEqual(obj.first_name, "")
        self.assertEqual(obj.last_name, "")

    def test_password_encryption(self):
        obj = User()
        obj.password = "password123"

        self.assertEqual(obj.password, md5("password123".encode()).hexdigest())

if __name__ == '__main__':
    unittest.main()
