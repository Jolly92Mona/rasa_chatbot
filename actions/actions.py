# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_house_price"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         print("I am from action py file")

         dispatcher.utter_message(text="Yes sure, can you tell me the location? ")

         return []



class ActionCovidCases(Action):

    def name(self) -> Text:
        return "action_corona_cases_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19india.org/data.json").json()

        entities = tracker.latest_message['entities']
        print("Last msg now", entities)
        state = None
        for e in entities:
            if e['entity'] == "state":
                state = e["value"]

        for data in response["statewise"]:
            if data["state"] == state.title():
                print(data)
                message = "Here is the status of Covid19 in "+ state+ " Reported on "+ data["lastupdatedtime"]+". Active Cases : " + data["active"] + " confirmed Cases : " + data["confirmed"] + " Recovered Cases : " + data[
                    "recovered"]


        print(message)
        dispatcher.utter_message(message)

        return []

class ActionDistrictZone(Action):

    def name(self) -> Text:
        return "action_zone_district_detect"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19india.org/zones.json").json()

        entities = tracker.latest_message['entities']
        print("Last msg now", entities)
        district = None
        for e in entities:
            if e['entity'] == "district":
                district = e["value"]

        for data in response["zones"]:
            if data["district"] == district:
                print(data)
                message = district+ " from state " + data["state"] + " Falls under zone : "+ data["zone"]


        print(message)
        dispatcher.utter_message(message)

        return []


class ActionDistrictZone(Action):

    def name(self) -> Text:
        return "action_zone_district_detect"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19india.org/zones.json").json()

        entities = tracker.latest_message['entities']
        print("Last msg now", entities)
        district = None
        for e in entities:
            if e['entity'] == "district":
                district = e["value"]

        for data in response["zones"]:
            if data["district"] == district:
                print(data)
                message = district+ " from state " + data["state"] + " Falls under zone : "+ data["zone"]


        print(message)
        dispatcher.utter_message(message)

        return []




class ActionVerify_symptoms(Action):

    def name(self) -> Text:
        return "action_verify_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity'] == 'symptoms':
                covidsymptoms = e['value']

            if covidsymptoms == "fever and chills":
                message = " If you have a fever, cough or other symptoms, you might have COVID-19. "
            if covidsymptoms == "sore throat n cough":
                message = "If you have sore throat and cough you should get yourself tested for covid19"
            if covidsymptoms == "vomiting":
                message = " Vomiting is one of the symptoms of Covid19, please get yourself checked. "
            if covidsymptoms == "headache":
                message = " If you have headache with body pain and fever, then please get yourself checked for Covid19"
            else:
                message = "Please provide more symptoms of your illness"

        dispatcher.utter_message(text=message)

        return []
