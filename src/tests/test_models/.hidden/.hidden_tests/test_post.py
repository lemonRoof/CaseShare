import unittest
from models.post import Post
import models

class TestPost(unittest.TestCase):
    def setUp(self):
        models.storage_t = "db"

    def test_init_with_kwargs(self):
        kwargs = {
            "id": "123",
            "created_at": "2023-01-01T00:00:00.000",
            "updated_at": "2023-01-02T00:00:00.000",
            "user_id": "456",
            "content": "Test post",
            "timestamps": "2023-01-03T00:00:00.000"
        }
        obj = Post(**kwargs)

        self.assertEqual(obj.id, "123")
        self.assertEqual(obj.created_at, datetime(2023, 1, 1, 0, 0, 0))
        self.assertEqual(obj.updated_at, datetime(2023, 1, 2, 0, 0, 0))
        self.assertEqual(obj.user_id, "456")
        self.assertEqual(obj.content, "Test post")
        self.assertEqual(obj.timestamps, datetime(2023, 1, 3, 0, 0, 0))

    def test_init_without_kwargs(self):
        obj = Post()

        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.content, "")
        self.assertEqual(obj.timestamps, "")

    def test_comments_property(self):
        obj = Post()
        comment = Comment(post_id=obj.id)
        models.storage.new(comment)
        models.storage.save()

        self.assertEqual(len(obj.comments), 1)
        self.assertEqual(obj.comments[0], comment)

    def test_likes_property(self):
        obj = Post()
        like = Like(post_id=obj.id)
        models.storage.new(like)
        models.storage.save()

        self.assertEqual(len(obj.likes), 1)
        self.assertEqual(obj.likes[0], like)

if __name__ == '__main__':
    unittest.main()
