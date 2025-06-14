#!/usr/bin/python3
"""
Unit tests for FileStorage class
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""
    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new(self):
        """Tests the new method"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_all(self):
        """Test the all method"""
        self.assertEqual(self.storage.all(), {})
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.assertEqual(len(self.storage.all()), 2)
        self.assertIsInstance(self.storage.all(), dict)

    def test_save(self):
        """Tests the save method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r', encoding='utf-8') as f:
            obj_dict = json.load(f)
            key = f"BaseModel.{obj.id}"
            self.assertIn(key, obj_dict)
            self.assertEqual(obj_dict[key]['__class__'], 'BaseModel')

    def test_reload(self):
        """Test the Reload method"""
        self.storage._FileStorage__objects = {}
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

        obj = BaseModel()
        key = f"BaseModel.{obj.id}"
        data = {key: obj.to_dict()}
        data[key]['__class__'] = 'UnkonwnClass'
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f)
            self.storage.reload()
            self.assertEqual(self.storage.all(), {})

if __name__ == '__main__':
    unittest.main()
