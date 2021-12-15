import requests
import unittest

BASE = "http://127.0.0.1:5000/v1/"

class TestBlacklistAPIs(unittest.TestCase):
    def test_put_blacklist_number(self):
        response = requests.put(BASE + "blacklist/3")
        self.assertEqual(response.status_code, 201)

    def test_delete_blacklist_number(self):
        response = requests.put(BASE + "blacklist/2")
        response = requests.delete(BASE + "blacklist/2")
        self.assertEqual(response.status_code, 204)

class TestFibonacciAPIs(unittest.TestCase):
    def test_fibonacci(self):
        response = requests.get(BASE + "fibonacci/5")
        self.assertEqual(response.json(), 5)

    def test_fibonacci_with_pagination(self):
        response = requests.get(BASE + "fibonacci/list/5/2")
        self.assertEqual(response.json(), [[0, 1], [1, 2], [5]])


if __name__ == '__main__':
    unittest.main()
