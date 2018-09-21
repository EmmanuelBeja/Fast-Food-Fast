"""app/tests_auth.py"""
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
        app = create_app(config_name="testing")

        return app


class TestAuth(TestBase):
    """ Tests for the Auth """
    def setUp(self):
        # pass in test configurations
        config_name = 'testing'
        app = create_app(config_name)
        self.register_user = json.dumps(dict(
            username="user1",
            password='Pass123',
            userRole='client',
            confirmpass='Pass123'))

        self.client = app.test_client()
        self.client.post(
            '/v1/signup',
            data=self.register_user,
            content_type='application/json')

    def test_registration(self):
        """ Test for user registration """
        resource = self.client.post(
            '/v1/signup',
            data=json.dumps(dict(
                username="user2",
                password='pass1234',
                userRole='client',
                confirmpass='pass1234')), content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Successful')

    def test_username_exist(self):
        """ Test if username exists """
        resource = self.client.post(
            '/v1/signup',
            data=json.dumps(dict(
                username="user1",
                password='pass1234',
                userRole='client',
                confirmpass='pass1234')), content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 400)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Username is taken.')

    def test_login(self):
        """ Test login """
        resource = self.client.post(
            '/v1/login',
            data=json.dumps(dict(username="user1", password='Pass123')),
            content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(
            data['message'].strip(),
            'You are successfully logged in')

    def test_wrong_login_username(self):
        """ Test login validation """
        resource = self.client.post(
            '/v1/login',
            data=json.dumps(dict(username="user5", password='Pass123')),
            content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 200)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'user does not exist')

    def test_wrong_login_details(self):
        """ Test login validation """
        resource = self.client.post(
                '/v1/login',
                data=json.dumps(dict(username="user1", password='')),
                content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 401)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Wrong username or password')

if __name__ == '__main__':
    unittest.main()
