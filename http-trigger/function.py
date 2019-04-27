import azure.functions as func
from .utils import *


def on_event(req: func.HttpRequest) -> func.HttpResponse:
    if health_check(req):
        return respond("It works")
    elif source(req) == "VM":
        if event_type(req) == "Migration":
            tweet(req)
            return respond("Posted")
        else:
            return respond("Other VM events ignored")
    else:
        return respond("Non-VM events ignored")
