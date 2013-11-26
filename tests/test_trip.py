import unittest

SEATS = 3
USER_NAME = "User_01"
START_POINT = "Turin"
END_POINT = "Turku"
from cshare.model import (Car, Trip, User)

class TestTrip(unittest.TestCase):
    def setUp(self):
        self.car = Car(SEATS)
        self.user = User(USER_NAME, self.car)

    def test_trip(self):
        trip = Trip(START_POINT, END_POINT, self.user)
        self.assertEqual(trip.get_start(), START_POINT)
        self.assertEqual(trip.get_end(), END_POINT)
        self.assertEqual(trip.get_user(), self.user)
