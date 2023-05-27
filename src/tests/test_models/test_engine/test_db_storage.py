#!/usr/bin/python3
"""Test if CRUD operations with a mysql database are working"""
import MySQLdb
import faker
import unittest
from models.engine.db_storage import DBStorage
from models.user import User
storage = DBStorage()
storage.reload()


class TestEngine(unittest.TestCase):
    """Create test cases for the database engine"""

    @classmethod
    def setUpClass(cls):
        """Create a MySQLdb connection object"""
        import os
        __db = os.getenv('CS_MYSQL_DB')
        __host = os.getenv('CS_MYSQL_HOST')
        __pwd = os.getenv('CS_MYSQL_PWD')
        __user = os.getenv('CS_MYSQL_USER')
        __env = os.getenv('CS_ENV')
        cls.conn = MySQLdb.connect(host=__host, user=__user, passwd=__pwd, db=__db, port=3306)
        cls.cur = cls.conn.cursor()

    @classmethod
    def tearDownClass(cls):
        """Close the db and the connection afterall"""
        cls.cur.close()
        cls.conn.close()

    def tearDown(self):
        self.cur.execute('DELETE FROM users;')
        self.conn.commit()
    

    def test_all_with_class(self):
        """Test if all returns a list of all objects of a certain class"""
        self.cur.execute('INSERT INTO users(id, first_name, last_name, email, password)\
                         VALUES("nothing", "nothing", "nothing", "nothing", "nothing")')
        self.cur.execute('INSERT INTO users(id, first_name, last_name, email, password)\
                         VALUES("some", "some", "some", "some", "some")')
        self.conn.commit()
        users = storage.all(User)
        self.assertEqual(len(users), 2)
        self.assertIn(users[0].email, ["nothing", "some"])
        self.assertIn(users[1].email, ["some", "nothing"])
    
    
    def test_all_with_class_name(self):
        """Test if storage.all works when passed a string instead of a class"""
        self.cur.execute('INSERT INTO users(id, first_name, last_name, email, password)\
                         VALUES("nothing", "nothing", "nothing", "nothing", "nothing")')
        self.cur.execute('INSERT INTO users(id, first_name, last_name, email, password)\
                         VALUES("some", "some", "some", "some", "some")')
        self.conn.commit()
        users = storage.all("User")
        self.assertEqual(len(users), 2)
        self.assertIn(users[0].email, ["nothing", "some"])
        self.assertIn(users[1].email, ["some", "nothing"])

    def test_all_with_invalid_class(self):
        objs = storage.all('Random')
        self.assertEqual(len(objs), 0)

    def test_save(self):
        user1 = User(email="nothing", password="nothing", first_name='nothing', last_name='nothing')
        storage.new(user1)
        storage.save()
        users = storage.all(User)
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].id, user1.id)
    
    def test_delete_with_obj(self):
        user1 = User(email="nothing", password="nothing", first_name='nothing', last_name='nothing')
        storage.new(user1)
        storage.save()
        users = storage.all(User)
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].id, user1.id)
        storage.delete(user1)
        storage.save()
        users = storage.all(User)
        self.assertEqual(len(users), 0)

    def test_delete_with_invalid_object(self):
        user1 = User(email="nothing", password="nothing", first_name='nothing', last_name='nothing')
        storage.new(user1)
        storage.save()
        users = storage.all(User)
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].id, user1.id)
        storage.delete(None)
        storage.save()
        users = storage.all(User)
        self.assertEqual(len(users), 1)
        pass

    def test_get_with_valid_class_and_id(self):
        user1 = User(email="nothing", password="nothing", first_name='nothing', last_name='nothing')
        user2 = User(email="some", password="some", first_name='some', last_name='some')
        storage.new(user1)
        storage.new(user2)
        storage.save()
        user = storage.get(User, user1.id)
        self.assertIsInstance(user, User)
        self.assertEqual(user.id, user1.id)


    def test_get_with_invalid_class(self):
        user1 = User(email="nothing", password="nothing", first_name='nothing', last_name='nothing')
        user2 = User(email="some", password="some", first_name='some', last_name='some')
        storage.new(user1)
        storage.new(user2)
        storage.save()
        user = storage.get(int, user1.id)
        self.assertIsNone(user)

    def test_get_with_invalid_object(self):
        user1 = User(email="nothing", password="nothing", first_name='nothing', last_name='nothing')
        user2 = User(email="some", password="some", first_name='some', last_name='some')
        storage.new(user1)
        storage.save()
        user = storage.get(User, user2.id)
        self.assertIsNone(user)

    def test_close(self):
        pass

    def test_count_with_valid_class(self):
        user1 = User(email="nothing", password="nothing", first_name='nothing', last_name='nothing')
        user2 = User(email="some", password="some", first_name='some', last_name='some')
        storage.new(user1)
        storage.new(user2)
        storage.save()
        n = storage.count(User)
        self.assertIsInstance(n, int)
        self.assertEqual(n, 2)

    def test_count_with_invalid_class(self):
        user1 = User(email="nothing", password="nothing", first_name='nothing', last_name='nothing')
        user2 = User(email="some", password="some", first_name='some', last_name='some')
        storage.new(user1)
        storage.new(user2)
        storage.save()
        n = storage.count(int)
        self.assertIsInstance(n, int)
        self.assertEqual(n, 0)

    def test_get_user_by_email(self):
        fake = faker.Faker()
        user1 = User(email=fake.email(), password=fake.password(),
                     first_name=fake.first_name(), last_name=fake.last_name())
        user2 = User(email=fake.email(), password=fake.password(),
                     first_name=fake.first_name(), last_name=fake.last_name())
        storage.new(user1)
        storage.new(user2)
        storage.save()
        user = storage.get_user_by_email(user1.email)
        self.assertIsInstance(user, User)
        self.assertEqual(user.id, user1.id)
        self.assertNotEqual(user.id, user2.id)