# action_default_fallback

# from typing import Any, Text, Dict, List
from rasa_sdk import Action
from rasa_sdk.events import UserUtteranceReverted


class ActionDefaultFallback(Action):
    def name(self):
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_default")
        return [UserUtteranceReverted()]
