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

    def test_order_creation(self):
        """Test API can create a order (POST request)"""
        requestdata1 = '?order_id=5&food_name=Pizza&food_price=1000'
        requestdata2 = '&client_name=Waititu&client_adress=Kwale'
        res = self.client().post('/v1/orders'+requestdata1+requestdata2)
        self.assertEqual(res.status_code, 201)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
