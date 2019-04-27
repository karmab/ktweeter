import logging

import azure.functions as func
import traceback
from .function import on_event

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        return on_event(req)
    except Exception as e:
        message = "Error processing event or posting update.\nMessage: {}".format(e)
        traceback.print_exc()
        logging.error(message)
        return func.HttpResponse(
                message,
                status_code=400
            )
