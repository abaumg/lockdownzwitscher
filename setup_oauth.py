import os
from twython import Twython
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read(
    os.path.join(
        os.path.dirname(__file__),
        'lockdownzwitscher.ini'
    )
)

# initialize Twitter client with consumer key and consumer secret
CONSUMER_KEY = cfg.get('twitter', 'consumerKey')
CONSUMER_SECRET = cfg.get('twitter', 'consumerSecret')
twitterclient = Twython(CONSUMER_KEY, CONSUMER_SECRET)

# obtain preliminary oAuth token and secret
auth = twitterclient.get_authentication_tokens()
OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

# output auth url and wait for user to obtain PIN
print('Visit {} to complete verification'.format(auth['auth_url']))
pin = int(input('Enter PIN:'))

# initialize Twitter client with consumer key, consumer secret, oAuth token and oAuth secret
twitterclient = Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# obtain final oAuth tokens
final_step = twitterclient.get_authorized_tokens(pin)
OAUTH_TOKEN = final_step['oauth_token']
OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']

print('oAuthToken={}'.format(OAUTH_TOKEN))
print('oAuthTokenSecret={}'.format(OAUTH_TOKEN_SECRET))