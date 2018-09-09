# app/__init__.py
from flask_api import FlaskAPI
from flask import request, jsonify, abort

# local import
from instance.config import app_config


def create_app(config_name):
    from app.models import Order

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    @app.route('/v1/orders', methods=['POST'])
    def orders():
        #POST
        order_id = request.args.get('order_id')
        food_name = str(request.args.get('food_name'))
        food_price = str(request.args.get('food_price'))
        client_name = str(request.args.get('client_name'))
        client_adress = str(request.args.get('client_adress'))

        if order_id:
            order = Order(order_id=order_id, food_name=food_name, food_price=food_price, client_name=client_name, client_adress=client_adress)
            result = order.save()
            response = jsonify(result)
            response.status_code = 201
            return response

    return app
