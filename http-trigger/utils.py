import azure.functions as func
import logging
import twitter
import json
import os


def health_check(req: func.HttpRequest) -> bool:
    return req.method == "GET"


def respond(body: str) -> func.HttpResponse:
    return func.HttpResponse(body, status_code=200)


def source(req: func.HttpRequest) -> str:
    jsonEvent = req.get_json()
    logging.info("karmab/kwteeter handling")
    logging.info(jsonEvent)
    if 'migration' in jsonEvent['message'].lower():
        return "VM"
    else:
        return "Unknown"


def event_type(req: func.HttpRequest) -> str:
    jsonEvent = req.get_json()
    if 'migration' in jsonEvent['message'].lower():
        return "Migration"
    else:
        return "Unknown"


def _envRead(key):
    return os.environ[key]


def tweet(req: func.HttpRequest):
    jsonEvent = req.get_json()
    charLimit = 230
    consumer_key = _envRead('consumer_key')
    consumer_secret = _envRead('consumer_secret')
    access_token = _envRead('access_token')
    access_token_secret = _envRead('access_token_secret')

    twitterClient = twitter.Api(consumer_key,
                                consumer_secret,
                                access_token,
                                access_token_secret)
    message = jsonEvent['lastTimestamp'] + ' : ' + jsonEvent['message']
    message = (message[:charLimit-3] +
               "...") if len(message) > charLimit else message
    twitterClient.PostUpdate(message)
