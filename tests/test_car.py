import unittest

from cshare.model import Car

class TestCar(unittest.TestCase):
    def test__no_seats(self):
        "A car must have at least one seat"
        self.assertRaises(Exception, Car, 0)

