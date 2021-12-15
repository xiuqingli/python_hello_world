from flask_restful import Resource, abort
import config


def get_fib_numbers(n: int):
    if n == 1:
        return [0, 1]
    if n == 2:
        return [0, 1, 1]
    fib_numbers = [0] * (n+1)
    fib_numbers[1] = 1
    fib_numbers[2] = 1
    for i in range(3, n+1):
        fib_numbers[i] = fib_numbers[i-1] + fib_numbers[i-2]
    return fib_numbers


def get_fib_number(nth_number: int):
    fib_numbers = get_fib_numbers(nth_number)
    fib_number = fib_numbers[nth_number]

    if config.blacklist_numbers.get(fib_number):
        abort(400, message = "The fibonacci number is in the blacklist!")
    return fib_number


def get_fib_numbers_with_pagination(nth_number: int, numbers_per_page: int):
    fib_numbers = get_fib_numbers(nth_number)
    whitelist_fib_numbers = []

    for i in range(len(fib_numbers)):
        if config.blacklist_numbers.get(fib_numbers[i]) is None:
            whitelist_fib_numbers.append(fib_numbers[i])

    return [whitelist_fib_numbers[i:i+numbers_per_page] for i in range(0, len(whitelist_fib_numbers), numbers_per_page)]


class Fibonacci(Resource):
    def get(self, nth_number):
        return get_fib_number(nth_number)


class FibonacciWithPagination(Resource):
    def get(self, nth_number, numbers_per_page=100):
        return get_fib_numbers_with_pagination(nth_number, numbers_per_page)
