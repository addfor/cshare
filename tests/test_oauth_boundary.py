import unittest
try:
    import cPickle as pickle
except:
    import pickle

import atom
import gdata.calendar.service
from gdata.auth import OAuthSignatureMethod
CONSUMER_KEY = "460112401320.apps.googleusercontent.com"
CONSUMER_SECRET = "8xBG6SVAhVRxCukmICwQm1SY"

# The client_id and client_secret obtained during registration are embedded in
# the source code of your application. In this context, the client_secret is
# obviously not treated as a secret.
# For further reference see the link below.
# https://developers.google.com/accounts/docs/OAuth2InstalledApp

class TestAuthSecret(unittest.TestCase):
    def setUp(self):
        self.client = gdata.calendar.service.CalendarService()

    def test_set_params(self):
        self.client.SetOAuthInputParameters(OAuthSignatureMethod.HMAC_SHA1,
                                            consumer_key=CONSUMER_KEY,
                                            consumer_secret=CONSUMER_SECRET)

    def test_get_token(self):
        self.test_set_params()
        token = self.client.FetchOAuthRequestToken()
        self.assertIsNotNone(token)
        return token

    def test_gen_auth_url(self):
        self.test_set_params()
        self.test_get_token()
        auth_url = self.client.GenerateOAuthAuthorizationURL()
        self.assertIsNotNone(auth_url)
        return auth_url

    def test_auth(self):
        with open("access_token.dat") as f:
            access_token = pickle.load(f)

        self.client.token_store.add_token(access_token)
        cal_list = self.client.GetAllCalendarsFeed()
        calendars = [cal.title.text for cal in cal_list.entry]
        self.assertTrue("CSHARE" in calendars)






