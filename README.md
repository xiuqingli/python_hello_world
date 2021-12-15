# Fibonacci Flask-Rest API App

I don't have any Python experience, the follow tutorial and some blog posts online are used to put together this app.

- https://flask-restful.readthedocs.io/en/latest/index.html
- https://www.youtube.com/watch?v=GMppyAPbLYk
- https://www.youtube.com/watch?v=vYquumk4nWw


In Mac: Install python3 and pip3

1. `$ pip3 install virtualenv`
2. `$ python3 -m venv .venv` (In the project)
3. `$ source .venv/bin/activate` (Activate virtual environment)
4. `$ pip3 install -r requirements.txt`
5. `$ flask run` (start the app)
6. `$ python3 app_test.py` (run test)

There are 4 api routes as requested.

Example of test APIs:
1. GET http://127.0.0.1:5000/v1/fibonacci/5
2. GET http://127.0.0.1:5000/v1/fibonacci/list/5/2
3. PUT http://127.0.0.1:5000/v1/blacklist/3
4. DELETE http://127.0.0.1:5000/v1/blacklist/2