import logging

import azure.functions as func
import traceback
from .function import on_event

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        if req.method == "GET":
            return func.HttpResponse(on_event("health", None),status_code=200)

        jsonEvent = req.get_json()
        logging.info(jsonEvent)
        if 'Created Migration' in jsonEvent['message']:
            event = 'Migration'
        else:
            event = 'Unknown'

        response = on_event(event, jsonEvent)

        if not response:
            return func.HttpResponse("Ignored.", status_code=200)
        else:
            return func.HttpResponse(on_event(event, jsonEvent), status_code=200)
    except Exception as e:
        message = "Error processing event or posting update.\nMessage: {}".format(e)
        traceback.print_exc()
        logging.error(message)
        return func.HttpResponse(
                message,
                status_code=400
            )
