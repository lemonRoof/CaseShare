import unittest
from models.video import Video
import models

class TestVideo(unittest.TestCase):
    def setUp(self):
        models.storage_t = "db"

    def test_init_with_kwargs(self):
        kwargs = {
            "id": "123",
            "created_at": "2023-01-01T00:00:00.000",
            "updated_at": "2023-01-02T00:00:00.000",
            "filename": "video.mp4",
            "post_id": 456
        }
        obj = Video(**kwargs)

        self.assertEqual(obj.id, "123")
        self.assertEqual(obj.created_at, datetime(2023, 1, 1, 0, 0, 0))
        self.assertEqual(obj.updated_at, datetime(2023, 1, 2, 0, 0, 0))
        self.assertEqual(obj.filename, "video.mp4")
        self.assertEqual(obj.post_id, 456)

    def test_init_without_kwargs(self):
        obj = Video()

        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)
        self.assertEqual(obj.filename, "")
        self.assertEqual(obj.post_id, "")

if __name__ == '__main__':
    unittest.main()
