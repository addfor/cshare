class User(object):
    def __init__(self, user, car=None):
        self._user = user
        self._car = car

    def get_user(self):
        return self._user

    def get_car(self):
        if self._car is None:
            raise AttributeError("This user haven't a car")
        return self._car
