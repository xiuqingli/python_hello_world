# Fibonacci Flask-Rest API App

I don't have any Python experience, the follow tutorial and some blog posts online are used to put together this app.

- https://flask-restful.readthedocs.io/en/latest/index.html
- https://www.youtube.com/watch?v=GMppyAPbLYk
- https://www.youtube.com/watch?v=vYquumk4nWw


In Mac: after install python3, pip3 and virtualenv

Run project: open a new tab, go to the project in the terminal
1. `$ python3 -m venv .venv` (In the project)
2. `$ source .venv/bin/activate` (Activate virtual environment)
3. `$ pip3 install -r requirements.txt`
4. `$ flask run` (start the app)

Run test: open a new tab, go to the project in the terminal
1. `$ source .venv/bin/activate` 
2. `$ python3 app_test.py` 

There are 4 API routes as requested.
Example of test APIs:
1. GET http://127.0.0.1:5000/v1/fibonacci/5
2. GET http://127.0.0.1:5000/v1/fibonacci/list/5/2
3. PUT http://127.0.0.1:5000/v1/blacklist/3
4. DELETE http://127.0.0.1:5000/v1/blacklist/2


**To improve:
- the blacklist_numbers should keep in a persistent storage (datatabase)
- to move fibonacci number generation code to a separate file with it's own unit test
- funtion returns the value from the Fibonacci sequence for a given number can use the implementation without generating the whole list of of numbers
- more test coverages for API routes 
