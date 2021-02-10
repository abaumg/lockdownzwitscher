import giphy_client
import io
import os
import random

import requests
from twython import Twython
from configparser import ConfigParser
from datetime import datetime
from dateutil import parser

# read configuration
cfg = ConfigParser()
cfg.read(
    os.path.join(
        os.path.dirname(__file__),
        'lockdownzwitscher.ini'
    )
)

# initialize Twitter client
twitterclient = Twython(
    cfg.get('twitter', 'consumerKey'),
    cfg.get('twitter', 'consumerSecret'),
    cfg.get('twitter', 'oAuthToken'),
    cfg.get('twitter', 'oAuthTokenSecret')
    )

# initialize Giphy client
giphy = giphy_client.DefaultApi()

# calculate remaining days
today = datetime.today().date()
until = parser.parse(cfg.get('countdown', 'date')).date()
days = (until-today).days

if days < 1:
    quit()

hashtag = random.choice(cfg.get('countdown', 'hashtags').split(','))
tweetText = 'Friendly Reminder:\nNoch {} Tage Lockdown!\n😊 {}'.format(days, hashtag)

# search GIF
api_response = giphy.gifs_search_get(
    cfg.get('giphy', 'apiKey'),
    days,
    limit=1,
    lang='de')

if (type(api_response) is giphy_client.InlineResponse200):
    imageurl = api_response.data[0].images.original.url

if imageurl:
    r = requests.get(imageurl)
    with io.BytesIO(r.content) as file:
        mediaresponse = twitterclient.upload_media(media=file)

twitterclient.update_status(
    status=tweetText, 
    media_ids=([mediaresponse['media_id']] if 'mediaresponse' in globals() else None)
    )