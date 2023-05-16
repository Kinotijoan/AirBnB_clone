#!/usr/bin/python3
"""Defines unittests for file_storage.py"""

import unittest
from models.base_model import BaseModel
import os
import models
from datetime import datetime
from time import sleep
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        # Test when there are no objects in the storage
        objects = self.storage.all()
        self.assertEqual(len(objects), 0)

        # Test when there are objects in the storage
        obj1 = BaseModel()
        obj2 = User()
        self.storage.new(obj1)
        self.storage.new(obj2)
        objects = self.storage.all()
        self.assertEqual(len(objects), 2)
        self.assertIn(f"BaseModel.{obj1.id}", objects)
        self.assertIn(f"User.{obj2.id}", objects)
        self.assertIs(objects[f"BaseModel.{obj1.id}"], obj1)
        self.assertIs(objects[f"User.{obj2.id}"], obj2)

    def test_new(self):
        # Test adding a new object to the storage
        obj = BaseModel()
        self.storage.new(obj)
        objects = self.storage.all()
        self.assertIn(f"BaseModel.{obj.id}", objects)
        self.assertIs(objects[f"BaseModel.{obj.id}"], obj)

    def test_save_and_reload(self):
        # Test saving and reloading objects from file
        obj1 = BaseModel()
        obj2 = User()
        obj3 = State()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.new(obj3)
        self.storage.save()

        # Create a new storage instance and reload data
        new_storage = FileStorage()
        new_storage.reload()
        objects = new_storage.all()

        # Verify that the reloaded objects match the original objects
        self.assertIn(f"BaseModel.{obj1.id}", objects)
        self.assertIn(f"User.{obj2.id}", objects)
        self.assertIn(f"State.{obj3.id}", objects)
        self.assertIsInstance(objects[f"BaseModel.{obj1.id}"], BaseModel)
        self.assertIsInstance(objects[f"User.{obj2.id}"], User)
        self.assertIsInstance(objects[f"State.{obj3.id}"], State)

    def test_classes(self):
        # Test the classes() method
        classes = self.storage.classes()
        self.assertIsInstance(classes, dict)
        self.assertIn("BaseModel", classes)
        self.assertIs(classes["BaseModel"], BaseModel)
        self.assertIn("User", classes)
        self.assertIs(classes["User"], User)

    def test_attributes(self):
        # Test the attributes() method
        attributes = self.storage.attributes()
        self.assertIsInstance(attributes, dict)
        self.assertIn("BaseModel", attributes)
        self.assertIsInstance(attributes["BaseModel"], dict)
        self.assertIn("id", attributes["BaseModel"])
        self.assertIs(attributes["BaseModel"]["id"], str)
        self.assertIn("User", attributes)
        self.assertIsInstance(attributes["User"], dict)
        self.assertIn("email", attributes["User"])
        self.assertIs(attributes["User"]["email"], str)


if __name__ == "__main__":
    unittest.main()
