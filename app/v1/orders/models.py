"""/app/v1/orders/models.py"""
from flask import jsonify, session

class Order(object):
    def __init__(self):
        """ Initialize empty Order list"""
        self.order_list = []
        self.notfound = None

    def create_order(self, food_id, client_id, client_adress, status):
        """Create order_item"""
        self.orders = {}

        self.orderId = len(self.order_list)
        self.orders['food_id'] = food_id
        self.orders['client_id'] = client_id
        self.orders['client_adress'] = client_adress
        self.orders['status'] = status
        self.orders['order_id'] = self.orderId + 1
        self.order_list.append(self.orders)
        return jsonify({"message": "Successful.", "Orders":self.order_list}), 201

    def get_orders(self):
       """ get all Orders """
       return jsonify({"message": "Successful.","Order": self.order_list}), 200

    def delete_order(self, order_id):
        """ delete Order """
        for order in self.order_list:
            if order['order_id'] == order_id:
                self.order_list.remove(order)
                return jsonify({"message": "Delete Successful.", "Orders":self.order_list}), 201
            self.notfound = True
        if self.notfound == True:
            return jsonify({"message": "No order with that id.", "Orders":self.order_list}), 404


    def update_order(self, order_id, food_id, client_id, client_adress, status):
        """ update Order """
        for order in self.order_list:
            if order['order_id'] == order_id:
                order['food_id'] = food_id
                order['client_id'] = client_id
                order['client_adress'] = client_adress
                order['status'] = status
                return jsonify({"message": "Update Successful.", "Orders":self.order_list}), 201
            self.notfound = True
        if self.notfound == True:
            return jsonify({"message": "No order with that id.", "Orders":self.order_list}), 404

    def get_order(self, order_id):
        """ get Order """
        for order in self.order_list:
            if order['order_id'] == order_id:
                return jsonify({"message": "Successful.", "Order":order}), 200
            self.notfound = True
            
        if self.notfound == True:
            return jsonify({"message": "No order with that id.", "Orders":self.order_list}), 404

    def is_loggedin(self):
        if 'client_name' in session:
            return True
        return False
