"""
app/models.py
"""


class Order(object):
    """ Order: performs order related opperations """

    def __init__(self, order_id, food_name, food_price, client_name, client_adress):
        """initialize """
        self.order_id = order_id
        self.food_name = food_name
        self.food_price = food_price
        self.client_name = client_name
        self.client_adress = client_adress



    def save(self):
        """ save data """
        order = {
            "order_id": self.order_id,
            "food_name": self.food_name,
            "food_price": self.food_price,
            "client_name": self.client_name,
            "client_adress": self.client_adress
        }

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

        orders = orders.append(order)

        return order

    def __repr__(self):
        return "<Order: {}>".format(self.order_id, self.food_name, self.food_price, self.client_name, self.client_adress)
