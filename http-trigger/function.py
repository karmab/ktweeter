from .kube_events import tweet
import json

def on_event(type: str, event: json) -> str:
    if type == "health":
        return "It works."
    elif type == "Migration":
        tweet(event)
        return "Posted."
