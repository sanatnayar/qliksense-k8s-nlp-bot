# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import os
import subprocess
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet


class ActionShowCR(Action):

    def name(self) -> Text:
        return "actionInsight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        schema = tracker.get_slot("cluster_element")
        print(schema)
        if schema != None:
            schema = schema.lower()
        if schema == "cr":
            result = subprocess.run(['qliksense','config','view'] , stdout=subprocess.PIPE)
            dispatcher.utter_message(result.stdout)
        elif schema == "crd":
            result = subprocess.run(['qliksense','operator','crd'] , stdout=subprocess.PIPE)
            dispatcher.utter_message(result.stdout)
        elif schema=="all":
            result = subprocess.run(['qliksense','config','list-contexts'] , stdout=subprocess.PIPE)
            dispatcher.utter_message(result.stdout)
        else:
            dispatcher.utter_message("Sorry I could not understand what you mean")
        return [SlotSet("cluster_element", None)]


class SetAttributeForm(FormAction):
    """Custom form action to fill all slots required to find specific type
    of healthcare facilities in a certain city or zip code."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "attribute_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["key", "value"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"key": self.from_entity(entity="key",
                                                  intent="inputKey"),
                "value": self.from_entity(entity="value",
                                             intent="inputValue")}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, print buttons for found facilities"""

        key = tracker.get_slot('key')
        value = tracker.get_slot('value')

        setCommand = key+'='+value
        print(setCommand)
        result = subprocess.run(['qliksense','config','set', setCommand] , stdout=subprocess.PIPE)
        dispatcher.utter_message(result.stdout)

        

        return[SlotSet("key", None), SlotSet("value", None)]


class ActionPeformPreflight(Action):

    def name(self) -> Text:
        return "preflightChecks"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        schema = tracker.get_slot("preflight")
        print(schema)
        if schema != None:
            schema = schema.lower()
            if schema == "deployments":
                result = subprocess.run(['qliksense','preflight','deployment'] , stdout=subprocess.PIPE)
                dispatcher.utter_message(result.stdout)
        else:
            result = subprocess.run(['qliksense','preflight','all'] , stdout=subprocess.PIPE)
            dispatcher.utter_message(result.stdout)
       
        return [SlotSet("preflight", None)]