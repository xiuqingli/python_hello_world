from flask import Flask
from flask_restful import Api
import config

from controllers.blacklist import BlackList 
from controllers.fibonacci import Fibonacci
from controllers.fibonacci import FibonacciWithPagination

app = Flask(__name__)
api = Api(app)

config.blacklist_numbers = {}

api.add_resource(Fibonacci, '/v1/fibonacci/<int:nth_number>')
api.add_resource(FibonacciWithPagination, '/v1/fibonacci/list/<int:nth_number>/<int:numbers_per_page>')
api.add_resource(BlackList, '/v1/blacklist/<int:number>')

if __name__ == '__main__':
    app.run()