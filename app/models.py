"""
app/models.py
"""

class Order(object):
    """ Order: performs order related opperations """

    def __init__(self, food_name, food_price, client_name, client_adress):
        """initialize """
        self.food_name = food_name
        self.food_price = food_price
        self.client_name = client_name
        self.client_adress = client_adress


    @staticmethod
    def get_all():
        """ get_all: lists all orders """
        orders = [
            {
                "order_id": 1,
                "food_name": "Pilau",
                "food_price": 350,
                "client_name": "Frank Oliel",
                "client_adress": 'Nyali, Kenya'
            },
            {
                "order_id": 2,
                "food_name": "French Fries",
                "food_price": 150,
                "client_name": "Logan Wolverine",
                "client_adress": 'Watamu, Kenya'
            },
            {
                "order_id": 3,
                "food_name": "Burger",
                "food_price": 150,
                "client_name": "Dead Cool",
                "client_adress": 'Old Town, Mombasa, Kenya'
            }
        ]
        return orders
