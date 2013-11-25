class Trip(object):
    def __init__(self, start, end, user):
        self._start = start
        self._end = end
        self._user = user

    def get_start(self):
        return self._start

    def get_end(self):
        return self._end

    def get_user(self):
        return self._user
