from cshare.model import (User, Car, Trip)


class Controller(object):
    def __init__(self, backend):
        self._backend = backend

    def create_profile(self, user, seats):
        car = Car(seats)
        self._user = User(user, car)
        return self._backend.get_access_url()

    def get_auth(self):
        return self._backend.get_access_credentials()

    def login(self):
        return self._backend.login()



