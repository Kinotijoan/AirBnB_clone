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

    def test_save(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

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
