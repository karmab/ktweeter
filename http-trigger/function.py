from .kube_events import tweet
import json

def on_event(source: str, cloud_event: json) -> str:
    if source == "health":
        return "It works."
    elif source == "VM":
        tweet(cloud_event)
        return "Posted."
