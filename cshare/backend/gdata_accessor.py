import gdata.calendar.service
from gdata.auth import OAuthSignatureMethod

CONSUMER_KEY = "460112401320.apps.googleusercontent.com"
CONSUMER_SECRET = "8xBG6SVAhVRxCukmICwQm1SY"
CALENDAR_NAME = "CSHARE"

class GData(object):
    def __init__(self, consumer_key=CONSUMER_KEY,
                 consumer_secret=CONSUMER_SECRET):
        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret
        self._auth_url = ""
        self._access_token = None
        self._client = gdata.calendar.service.CalendarService()
        self._client.SetOAuthInputParameters(OAuthSignatureMethod.HMAC_SHA1,
                                            consumer_key=CONSUMER_KEY,
                                            consumer_secret=CONSUMER_SECRET)


    def create_auth(self):
        self._client.FetchOAuthRequestToken()
        self._auth_url = self._client.GenerateOAuthAuthorizationURL()

        yield self._auth_url

        self._access_token = self._client.UpgradeToOAuthAccessToken()
        yield self._access_token

    def login(self, access_token):
        self._client.token_store.add_token(access_token)
