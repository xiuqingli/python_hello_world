from flask_restful import Resource
import config

class BlackList(Resource):
    def put(self, number):
        if number > 0:
            config.blacklist_numbers[number] = number
        return '', 201

    def delete(self, number):
        config.blacklist_numbers.pop(number)
        return '', 204
