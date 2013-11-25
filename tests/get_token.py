try:
    import cPickle as pickle
except:
    import pickle

import gdata.calendar.service
from gdata.auth import OAuthSignatureMethod
CONSUMER_KEY = "460112401320.apps.googleusercontent.com"
CONSUMER_SECRET = "8xBG6SVAhVRxCukmICwQm1SY"


if __name__ == "__main__":
    client = gdata.calendar.service.CalendarService()
    client.SetOAuthInputParameters(OAuthSignatureMethod.HMAC_SHA1,
                                   consumer_key=CONSUMER_KEY,
                                   consumer_secret=CONSUMER_SECRET)
    token =client.FetchOAuthRequestToken()
    auth_url = client.GenerateOAuthAuthorizationURL()
    print "Manually Browse the following url and then press Enter"
    print auth_url
    raw_input("Press Enter when ready")
    access_token = client.UpgradeToOAuthAccessToken()
    with open("access_token.dat", 'w') as f:
        pickle.dump(access_token, f)



