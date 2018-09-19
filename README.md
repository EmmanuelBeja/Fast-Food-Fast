# Fast-Food-Fast
<<<<<<< HEAD
[![Build Status](https://travis-ci.org/EmmanuelBeja/Fast-Food-Fast.svg?branch=ft-ordercreation-160341546)](https://travis-ci.org/EmmanuelBeja/Fast-Food-Fast) [![Coverage Status](https://coveralls.io/repos/github/EmmanuelBeja/Fast-Food-Fast/badge.svg?branch=ft-ordercreation-160341546)](https://coveralls.io/github/EmmanuelBeja/Fast-Food-Fast?branch=ft-ordercreation-160341546)

A food delivery service app for a restaurant.

## Place Order:

This branch holds code to place an order


## Routes

 - POST /v1/orders
=======
[![Build Status](https://travis-ci.org/EmmanuelBeja/Fast-Food-Fast.svg?branch=ft-allorders-160341465)](https://travis-ci.org/EmmanuelBeja/Fast-Food-Fast) [![Coverage Status](https://coveralls.io/repos/github/EmmanuelBeja/Fast-Food-Fast/badge.svg?branch=API)](https://coveralls.io/github/EmmanuelBeja/Fast-Food-Fast?branch=API)

A platform where people get to order food added by the admin. The admin can then accept decline or complete the orders made.

>>>>>>> API


 To interact with the api endpoints, visit the link [here](https://emmanuelbeja-fast-food-fast.herokuapp.com/v1/orders)<br>

## Use the following endpoints to perform the specified tasks

| 	Endpoint                       | Functionality                                  |                  
| ---------------------------------| -----------------------------------------------|
| POST /v1/orders                  | Create an order                                |
| GET /v1/orders                   | Retrieve posted orders                         |
| PUT /v1/orders/<int:id>          | Update a specific order                        |                         
| GET /v1/orders/<int:id>          | Get a specific posted order                    |
| DELETE /v1/orders/<int:id>       | DELETE a specific posted order                 |



## Application Features

1. Create orders
2. view, accept, decline and complete an order.
3. Create, edit and delete Food items

<br>

**Users can do the following**

* Users can create an account and log in.
* Users can order food.
* Users can view history of their order.

**Admin can do the following**
* Admin can add, edit and delete food items.
* Admin can view, accept, decline and complete an order.

## How to Test Manually
1. Clone the project to your local machine <br>
		` https://github.com/EmmanuelBeja/Fast-Food-Fast.git`
2. Create Virtual Environment <br>
		`virtualenv venv`
3. Activate Virtual ENvironment<br>
		`source venv/bin/activate`
4. Install Dependencies<br>
		`(venv)$ pip3 install -r requirements.txt` <br>
		`(venv)$ pip3 freeze > requirements.txt` <br>
5. Run the app <br>
		`python3 run.py`<br>
6. Run tests <br>
		`pytest`
		<br>
## How to Contribute to this project?

1. Fork the project to your github account.

2. Clone it to your local machine.

3. Create a feature branch from develop branch :

4. git checkout -b `ft-name-of-the-feature`

5. Update and Push the changes to github.

6. git push origin `ft-name-of-the-feature`

7. Create Pull Request to my develop branch as base branch.
