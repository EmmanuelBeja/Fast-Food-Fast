# Fast-Food-Fast


A platform where people get to order food added by the admin. The admin can then accept decline or complete the orders made.

  To interact with the app UI, click link
  [here](https://emmanuelbeja.github.io/Fast-Food-Fast/)<br>

   To interact with the api endpoints, visit the link [here](https://emmanuelbeja-fast-food-fast.herokuapp.com/)<br>

## Use the following endpoints to perform the specified tasks

  | 	Endpoint                       | Functionality                                  |                  
  | ---------------------------------| -----------------------------------------------|
  | POST /v1/orders                  | Create an order                                |
  | GET /v1/orders                   | Retrieve posted orders                         |
  | PUT /v1/orders/<int:order_id>    | Update a specific order                        |                         
  | GET /v1/orders/<int:order_id>    | Get a specific posted order                    |
  | DELETE /v1/orders/<int:order_id> | DELETE a specific posted order                 |
  | POST /v1/food                    | Create food item                               |
  | GET /v1/food                     | Retrieve posted food                           |
  | PUT /v1/food/<int:food_id>       | Update a specific food                         |                         
  | GET /v1/food/<int:food_id>       | Get a specific posted food                     |
  | DELETE /v1/food/<int:food_id>    | DELETE a specific posted food                  |
  | POST /v1/signup                  | Sign up User                                   |
  | POST /v1/login                   | Login User                                     |
  | PUT /v1/users/<int:id>           | Update a specific user                         |                         
  | GET /v1/users/<int:id>           | Get a specific signed up user                  |
  | DELETE /v1/users/<int:id>        | DELETE a specific signed up user               |
  | GET /v1/users                    | Get all signed up users                        |
  | GET /v1/auth/logout              | Logout a user                                  |


## Usage

### Users:

POST /v1/signup - signup user
<br>
{
	"username": "Beja",
	"userphone": "0712991415",
	"password": "pass1234",
	"userRole": "client",
	"confirmpass": "pass1234"
}
<br>
GET /v1/auth/logout  - logout user
<br>
POST /v1/login  - login user
<br>
{
	"username": "Beja",
	"password": "pass1234"
}
<br>
GET /v1/users/1  - Get user by id
<br>
GET /v1/users  - Get all users
<br>
DELETE /v1/users/1  - Delete a user
<br>
UPDATE /v1/users/1  - Update user details
<br>
{
	"username": "Chayu",
	"userphone": "0712991416",
	"password": "pass12345",
	"userRole": "client",
	"confirmpass": "pass12345"
}
<br>
### Food:
<br>
GET /v1/food  - Get ll food
<br>
POST /v1/food  - Create a food item
<br>
{
	"food_name": "rice",
	"food_price": 200,
	"food_image": "img1.jpg"
}
<br>
GET /v1/food/1  - Get a food item by food id
<br>
PUT /v1/food/1  - Edit food item details
<br>
{
	"food_name": "tilapia",
	"food_price": 350,
	"food_image": "tilapia.jpg"
}
<br>
DELETE /v1/food/1  -Delete a food item
<br>
### Orders:
<br>
POST /v1/orders  - Create an order
<br>
{
	"food_id": 1,
	"client_id": 2,
	"client_adress": "Kisumu"
}
<br>
GET /v1/orders -Get all order
<br>
PUT /v1/userorders/1  - Edit an order
<br>
{
	"food_id": 1,
	"client_id": 1,
	"client_adress": "Thika",
	"status": "Accepted"
}
<br>
DELETE /v1/orders/1  -Delete an order
<br>
GET /v1/orders/1  - Get an order by order id


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
		` https://github.com/EmmanuelBeja/Fast-Food-Fast-API.git`
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
