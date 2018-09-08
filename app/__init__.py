# app/__init__.py
from flask_api import FlaskAPI
from flask import request, jsonify, abort

# local import
from instance.config import app_config


def create_app(config_name):
    from app.models import Order

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    @app.route('/v1/orders/', methods=['GET'])
    def orders():
        # GET
        orders = Order.get_all()
        results = []

        for index in range(len(orders)):
            for key in orders[index]:
                print(orders[index][key])
                obj = orders[index][key]
                results.append(obj)
        response = jsonify(results)
        response.status_code = 200
        return response

    return app
