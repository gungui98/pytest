from unittest import TestCase
from models.MyModel import Number


class TestNumber(TestCase):
    def test_plus(self):
        number = Number()
        assert number.plus(1, 2) == 3
