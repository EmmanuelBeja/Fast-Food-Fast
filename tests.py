"""
tests.py
"""
import unittest

from app import create_app


class OrderTestCase(unittest.TestCase):
    """This class represents the order test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.order = {
            "id": 1,
            "food_name": "Pilau",
            "food_price": 350,
            "client_name": "Frank Oliel",
            "client_adress": "Nyali"
        }

    def test_api_can_get_all_orders(self):
        """Test API can get all orders (GET request)."""
        res = self.client().get('/v1/orders/')
        self.assertEqual(res.status_code, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
