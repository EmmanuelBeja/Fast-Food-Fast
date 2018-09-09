# app/__init__.py
from flask_api import FlaskAPI
from flask import request, jsonify, abort

# local import
from instance.config import app_config


def create_app(config_name):
    from app.models import Order

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    @app.route('/v1/orders/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
    def order_manipulation(order_id, **kwargs):
        # retrieve an order using it's order_id
        #get all orders first
        orders = Order.get_all()
        #filter through to get specific order
        for index in range(len(orders)):
            if orders[index]['order_id'] == order_id:
                order = orders[index]

        if not order:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            order = Order(order_id=order_id, food_name='', food_price='', client_name='', client_adress='')
            orders = order.delete()

            results = []

            for index in range(len(orders)):
                for key in orders[index]:
                    print(orders[index][key])
                    obj = orders[index][key]
                    results.append(obj)

            message = {
            "message": "order {} deleted successfully".format(order.order_id)
            }
            print(message)

            response = jsonify(results)
            response.status_code = 200
            return response

        elif request.method == 'PUT':
            food_name = str(request.data.get('food_name'))
            food_price = str(request.data.get('food_price'))
            client_name = str(request.data.get('client_name'))
            client_adress = str(request.data.get('client_adress'))

            order['food_name'] = food_name
            order['food_price'] = food_price
            order['client_name'] = client_name
            order['client_adress'] = client_adress

            order = Order(order_id=order_id, food_name=order['food_name'], food_price=order['food_price'], client_name=order['client_name'], client_adress=order['client_adress'])
            result = order.save()
            response = jsonify(result)
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'order_id': order['order_id'],
                'food_name': order['food_name'],
                'food_price': order['food_price'],
                'client_name': order['client_name'],
                'client_adress': order['client_adress']
            })
            response.status_code = 200
            return response

    return app
