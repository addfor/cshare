import unittest

from cshare.model import Car

class TestCar(unittest.TestCase):
    def test_no_seats(self):
        "A car must have at least one seat"
        self.assertRaises(Exception, Car, 0)

    def test_car_creation(self):
        "Testing average case for car objects"
        for i in xrange(1,10):
            car = Car(i)
            self.assertEqual(i, car.get_seats())

