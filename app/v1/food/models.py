"""/app/v1/food/models.py"""
from flask import jsonify, session

class Food(object):
    def __init__(self):
        """ Initialize empty Order list"""
        self.food_list = []
        self.notfound = None

    def create_food(self, food_name, food_price, food_image):
        """Create food_item"""
        self.foods = {}

        self.foodId = len(self.food_list)
        self.foods['food_name'] = food_name
        self.foods['food_price'] = food_price
        self.foods['food_image'] = food_image
        self.foods['food_id'] = self.foodId + 1
        self.food_list.append(self.foods)
        return jsonify({"message": "Successful.", "Food":self.food_list}), 201

    def get_foods(self):
       """ get all Foods """
       return jsonify({"message": "Successful.","Food": self.food_list}), 200

    def delete_food(self, food_id):
        """ delete Food """
        for food in self.food_list:
            if food['food_id'] == food_id:
                self.food_list.remove(food)
                return jsonify({"message": "Delete Successful.", "Food":self.food_list}), 201
            self.notfound = True
        if self.notfound == True:
            return jsonify({"message": "No food with that id.", "Food":self.food_list}), 404


    def update_food(self, food_id, food_name, food_price, food_image):
        """ update Food """
        for food in self.food_list:
            if food['food_id'] == food_id:
                food['food_name'] = food_name
                food['food_price'] = food_price
                food['food_image'] = food_image
                return jsonify({"message": "Update Successful.", "Food":self.food_list}), 201
            self.notfound = True
        if self.notfound == True:
            return jsonify({"message": "No food with that id.", "Food":self.food_list}), 404

    def get_food(self, food_id):
        """ get Food """
        for food in self.food_list:
            if food['food_id'] == food_id:
                return jsonify({"message": "Successful.", "Food":food}), 200
            self.notfound = True
        if self.notfound == True:
            return jsonify({"message": "No food with that id.", "Food":self.food_list}), 404

    def is_loggedin(self):
        if 'client_name' in session:
            return True
        return False
