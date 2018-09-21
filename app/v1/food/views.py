"""/app/v1/food/views.py"""
from flask import Flask, request, flash, redirect, url_for, jsonify, session

"""local imports """
from . import food_api
from .models import Food

"""instantiate class"""
foodObject = Food()

"""Food views"""
@food_api.route('/food', methods=["POST"])
def food():
    """ Method to create and retrieve food."""
    data = request.get_json()
    food_name = data['food_name']
    food_price = data['food_price']
    food_image = data['food_image']
    res = foodObject.create_food(food_name, food_price,food_image)
    return res
