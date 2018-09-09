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

    def test_api_can_get_order_by_id(self):
        """Test API can get a single order by using it's order_id."""
        rv = self.client().get('/v1/orders/1')
        self.assertEqual(rv.status_code, 200)

    def test_order_can_be_edited(self):
        """Test API can edit an existing order. (PUT request)"""
        rv = self.client().put(
            '/v1/orders/1',
            data={
                "food_name": "French Fries",
                "food_price": 150,
                "client_name": "Logan Wolverine",
                "client_adress": "Watamu, Kenya"
            })
        self.assertEqual(rv.status_code, 200)

    def test_order_deletion(self):
        """Test API can delete an existing order. (DELETE request)."""
        res = self.client().delete('/v1/orders/1')
        self.assertEqual(res.status_code, 200)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
