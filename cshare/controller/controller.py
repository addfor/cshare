from cshare.model import (User, Car, Trip)


class Controller(object):
    def __init__(self, backend):
        self._backend = backend

    def create_profile(self, user, seats):
        car = Car(seats)
        self._user = User(user, car)
        return self._backend.get_access_url()

    def get_auth(self):
        return self._backend.get_auth()

    def login(self):
        return self._backend.login()


if __name__ == "__main__":
    from google_facade import GDataFacade
    from cshare.backend import GData
    backend = GData()
    api = GDataFacade(backend)
    c = Controller(api)
    #print c.create_profile("Dani", 3)
    #raw_input()
    #c.get_auth()
    c.login()




