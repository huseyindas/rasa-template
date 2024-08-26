import json
from typing import Text, List, Dict, Any, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, SlotSet, EventType

class ActionListProducts(Action):
    def name(self) -> Text:
        return "action_list_products"
    
    def get_carousel(self, json_data):
        test_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": json_data
            }
        }
        return test_carousel

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        with open("/app/actions/carousel.json", "r") as file:
            json_data = json.loads(file.read())
            carousel = self.get_carousel(json_data)
            dispatcher.utter_message(attachment=carousel)


class ActionSearchProducts(FormAction):
    def name(self) -> Text:
        return "action_search_products"
    
    def search_products(self, products, query):
        results = []
        query_lower = query.lower()
        for product in products:
            title = product.get('title', '').lower()
            description = product.get('description', '').lower()
            if query_lower in title or query_lower in description:
                results.append(product)
        return results
    
    def get_carousel(self, json_data):
        test_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [{
                    "title": item["title"],
                    "subtitle": item["description"],
                    "image_url": item["image"],
                    "buttons": [ 
                        {
                        "title": f'${item["price"]}',
                        "url": "/",
                        "type": "web_url"
                        }
                    ]
                } for item in json_data]
            }
        }
        return test_carousel
    
    @staticmethod
    def required_slots(tracker):
        return [
            "query"
        ]
    
    async def validate(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> List[EventType]:

        requested_slot = tracker.slots.get("requested_slot", None)
        text = tracker.latest_message.get("text")

        
        if requested_slot == "query":
            return [SlotSet("query", text)]
        
        return []
    
    def request_next_slot(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: Dict[Text, Any],
    ) -> Optional[List[EventType]]:
        
        query = tracker.slots.get("query", None)

        if query is None:
            dispatcher.utter_message("Write search keywords please: ")
            return [SlotSet("requested_slot", "query")]
        

    async def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        query = tracker.slots.get("query", None)

        with open("/app/actions/products.json", "r") as file:
            json_data = json.loads(file.read())
            result = self.search_products(json_data, query)
            if result:
                carousel = self.get_carousel(result)
                dispatcher.utter_message(attachment=carousel)
            else:
                dispatcher.utter_message("I can't find products on my database.")

        return self.deactivate() + [AllSlotsReset()]