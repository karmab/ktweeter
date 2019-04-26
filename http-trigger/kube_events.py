import twitter
import json
import os

def _envRead(key):
    return os.environ[key]

def tweet(jsonEvent: json):
    charLimit = 230
    consumer_key        = _envRead('consumer_key')
    consumer_secret     = _envRead('consumer_secret')
    access_token        = _envRead('access_token')
    access_token_secret = _envRead('access_token_secret')

    twitterClient = twitter.Api(consumer_key,
                    consumer_secret,
                    access_token,
                    access_token_secret)
    message = jsonEvent['lastTimestamp'] + ' : ' + jsonEvent['message']
    message = (message[:charLimit-3] + "...") if len(message) > charLimit else message
    twitterClient.PostUpdate(message)
