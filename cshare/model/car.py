class Car(object):
    def __init__(self, seats):
        if seats == 0:
            raise AttributeError("A car must have at least one seat")
        self._seats = seats

    def get_seats(self):
        return self._seats
