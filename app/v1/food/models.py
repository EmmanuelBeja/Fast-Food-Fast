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
