from django.test import TestCase
from user.func.math import add_numbers
from user.func.math import minus_numbers


class TestMath(TestCase):
    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_add_numbers_negative(self):
        result = add_numbers(-2, -3)
        self.assertEqual(result, -5)

    def test_minus_numbers(self):
        result = minus_numbers(2, 3)
        self.assertEqual(result, -1)

    def test_minus_numbers_negative(self):
        result = minus_numbers(-2, -3)
        self.assertEqual(result, 1)