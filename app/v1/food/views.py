"""/app/v1/food/views.py"""
from flask import Flask, request, flash, redirect, url_for, jsonify, session

"""local imports """
from . import food_api
from .models import Food

"""instantiate class"""
foodObject = Food()

"""Food views"""
@food_api.route('/food', methods=["GET", "POST"])
def food():
    """ Method to create and retrieve food."""
    if request.method == "POST":
        data = request.get_json()
        food_name = data['food_name']
        food_price = data['food_price']
        food_image = data['food_image']
        res = foodObject.create_food(food_name, food_price,food_image)
        return res
    data = foodObject.get_foods()
    return data

@food_api.route('/food/<int:food_id>', methods=['GET', 'PUT', 'DELETE'])
def food_manipulation(food_id, **kwargs):
    """ GET/PUT/DEL food """

    if request.method == 'DELETE':
        #DELETE
        res = foodObject.delete_food(food_id)
        return res

    elif request.method == 'PUT':
        #PUT
        data = request.get_json()
        food_name = data['food_name']
        food_price = data['food_price']
        food_image = data['food_image']
        res = foodObject.update_food(food_id, food_name, food_price, food_image)
        return res

    else:
        # GET
        res = foodObject.get_food(food_id)
        return res
