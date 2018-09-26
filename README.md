# Fast-Food-Fast

  A platform where people get to order food added by the admin. The admin can then accept decline or complete the orders made.

  To interact with the app UI, click link
  [here](https://emmanuelbeja.github.io/Fast-Food-Fast/)<br>

  To interact with the api endpoints, visit the link and add endpoints [here](https://emmanuelbeja-fast-food-fast.herokuapp.com/)<br>

  API documentation [here](https://documenter.getpostman.com/view/5399899/RWaPv6zH)

  ## Use the following endpoints to perform the specified tasks

  | 	Endpoint                       | Functionality                                  |                  
  | ---------------------------------| -----------------------------------------------|
  | POST /v1/orders                  | Create an order                                |
  | GET /v1/orders                   | Retrieve posted orders                         |
  | PUT /v1/orders/<int:order_id>    | Update a specific order                        |                         
  | GET /v1/orders/<int:order_id>    | Get a specific posted order                    |
  | DELETE /v1/orders/<int:order_id> | DELETE a specific posted order                 |
  | GET /v1/userorders/<int:order_id>| DELETE a specific user's orders                |
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

  ## Application Features

  1. Create orders.
  2. view, accept, decline and complete an order.
  3. Create, edit and delete Food items.
  4. Authentication.
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
