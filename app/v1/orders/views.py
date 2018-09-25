"""/app/v1/orders/views.py"""
from flask import Flask, request, flash, redirect, url_for, jsonify, session
from . import orders_api
from app.models import Order

"""instantiate class"""
orderObject = Order()


@orders_api.route('/orders', methods=["GET", "POST"])
def order():
    """ Method to create and retrieve order."""
    if request.method == "POST":
        data = request.get_json()
        food_id = data['food_id']
        client_id = data['client_id']
        client_adress = data['client_adress']
        status = "pending"
        res = orderObject.create_order(
            food_id,
            client_id,
            client_adress,
            status)
        return res
    data = orderObject.get_orders()
    return data


@orders_api.route('/orders/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def order_manipulation(order_id, **kwargs):
    """ GET/PUT/DEL order """

    if request.method == 'DELETE':
        # DELETE
        res = orderObject.delete_order(order_id)
        return res

    elif request.method == 'PUT':
        # PUT
        data = request.get_json()
        data = request.get_json()
        food_id = data['food_id']
        client_id = data['client_id']
        client_adress = data['client_adress']
        status = data['status']
        res = orderObject.update_order(
            order_id,
            food_id,
            client_id,
            client_adress,
            status)
        return res

    else:
        # GET
        res = orderObject.get_order(order_id)
        return res


@orders_api.route('/userorders/<int:client_id>', methods=['GET'])
def userorders(client_id, **kwargs):
    """ get a users orders"""
    res = orderObject.get_user_orders(client_id)
    return res        
