import os

try:
    import cPickle as pickle
except:
    import pickle

SETTINGS_PATH = os.path.abspath(os.path.expanduser("~/.cshare"))

class GoogleAdapter(object):
    def __init__(self, accessor):
        self._api = accessor
        self._authenticator = None
        self._auth_url = None
        self._auth_token = None
        self._token_path = os.path.join(SETTINGS_PATH, "token.dat")
        self._create_user_settings()

    def _create_user_settings(self):
        #TODO this isn't portable, use ENVIRON!
        if not os.path.exists(SETTINGS_PATH):
            os.mkdir(SETTINGS_PATH)

    def get_access_url(self):
        self._authenticator = self._api.create_auth()
        self._auth_url = self._authenticator.next()
        return self._auth_url

    def get_access_credentials(self):
        self._auth_token = self._authenticator.next()
        self._store_credential()
        return self._auth_token

    def _store_credential(self):
        with open(self._token_path, "w") as token_file:
            pickle.dump(self._auth_token, token_file)

    def login(self):
        if self._auth_token is None:
            with open(self._token_path) as token_file:
                self._auth_token = pickle.load(token_file)
        self._api.login(self._auth_token)
