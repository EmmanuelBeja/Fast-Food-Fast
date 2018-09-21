"""app/tests_orders.py"""
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
        self.create_order = json.dumps(dict(
                food_id=1,
                client_id=1,
                client_adress='Likoni',
                status='pending'))
        self.client = app.test_client()
        self.client.post(
            '/v1/orders',
            data=self.create_order,
            content_type='application/json')

    def test_order_creation(self):
        """ Test for order creation """
        resource = self.client.post(
                '/v1/orders',
                data=self.create_order,
                content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Successful.')

    def test_get_all_orders(self):
        """ Test for getting all orders """
        resource = self.client.get(
            '/v1/orders',
            data=json.dumps(dict()),
            content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 200)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Successful.')

    def test_get_order_by_order_id(self):
        """ Test for getting specific orders """
        resource = self.client.get('/v1/orders/1')
        self.assertEqual(resource.status_code, 200)

    def test_order_can_be_edited(self):
        """ test order can be edited """
        resource = self.client.put(
                '/v1/orders/1',
                data=self.create_order,
                content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Update Successful.')

    def test_order_deletion(self):
        """Test API can delete an existing order. (DELETE request)."""
        res = self.client.delete('/v1/orders/1')
        self.assertEqual(res.status_code, 201)

if __name__ == '__main__':
    unittest.main()
