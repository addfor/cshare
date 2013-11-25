import unittest

from cshare.model import (Car, Profile)
USER = "User_01"
SEATS = 3

class TestProfile(unittest.TestCase):
    def setUp(self):
        self.car = Car(SEATS)

    def test_user_name(self):
        profile = Profile(USER)
        user = profile.get_user()
        self.assertEqual(user, USER)

    def test_no_car(self):
        profile = Profile(USER)
        self.assertRaises(AttributeError, profile.get_car)

    def test_profile(self):
        profile = Profile(USER, self.car)
        self.assertEqual(SEATS, profile.get_car().get_seats())

