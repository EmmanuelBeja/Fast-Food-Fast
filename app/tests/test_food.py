"""app/tests_food.py"""
import unittest
import os
import json
from flask import url_for, abort, session
from flask_testing import TestCase
from app import create_app

class TestBase(TestCase):
    """ Tests Base """

    def create_app(self):
        # pass in test configurations
        config_name = 'testing'
        app = create_app(config_name)

        return app

class TestOrders(TestBase):
    """ Tests for the Orders """
    def setUp(self):
        # pass in test configurations
        app = create_app(config_name="testing")
        self.create_food = json.dumps(dict(food_name="mchele",
                food_price= 200, food_image='mchele.jpg'))
        self.client = app.test_client()
        self.client.post('/v1/food', data = self.create_food, content_type='application/json')

    def test_food_creation(self):
        """ Test for food creation """
        resource = self.client.post('/v1/food',
                data=self.create_food, content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Successful.')

if __name__ == '__main__':
    unittest.main()
