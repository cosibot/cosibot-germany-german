# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List
import requests

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction


class DecsisAPI:

    def search(self, description: str, region: str):

        try:
            host = "api.data.decsis.cloud"
            query_fields = "[{\"cases_per_population\": \"field\"}, {\"death_rate\": \"field\"},{\"deaths\": \"field\"},{\"confirmed_accum\": \"field\"},{\"district\": \"field\"},{\"state\": \"field\"},{\"nuts\": \"field\"},{\"district_type\": \"field\"},{\"date_day\": \"field\"}]"

            # today = date.today()
            # query_filters = "[{\"date_day\":\"" + today.strftime("%Y-%m-%d")+"\"},{\""+ str(description) + "\":\""+ str(state_district) + "\"}]"
            query_filters = "[{\"" + str(description) + "\":\"" + str(region) + "\"}]"

            request_url = "https://" + host + "/api/v1/dataset/de_rki_covid19_landkreis?query={\"fields\":" + str(query_fields) + ", \"filters\":" + str(query_filters) + "}&format=json&limit=200&last-data=date_day"

            response = requests.get(url=request_url)
            json_response = (response.json())

            if (len(json_response) > 1):
                stats = json_response[0]
                stats['code'] = response.status_code
                stats['has_data'] = True
                stats['confirmed_accum'] = str(sum(c["confirmed_accum"] for c in json_response))
                stats['date_day'] = json_response[0]["date_day"]
                stats['deaths'] = str(sum(c["deaths"] for c in json_response))
                stats['state'] = json_response[0]["state"]

                return stats
            elif (len(json_response) == 1):
                stats = json_response[0]
                stats['code'] = response.status_code
                stats['had_data'] = True
                return stats
            else:
                # date_search = datetime.today() - timedelta(days=1)
                query_filters = "[{\"" + str(description) + "\":\"" + str(region) + "\"}]"

                request_url = "https://" + host + "/api/v1/dataset/de_rki_covid19_landkreis?query={\"fields\":" + str(query_fields) + ", \"filters\":" + str(query_filters) + "}&format=json&limit=200&last-data=date_day"
                response = requests.get(url=request_url)

                if (len(json_response) > 1):
                    stats = json_response[0]
                    stats['code'] = response.status_code
                    stats['has_data'] = True
                    stats['confirmed_accum'] = str(sum(c["confirmed_accum"] for c in json_response))
                    stats['date_day'] = json_response[0]["date_day"]
                    stats['deaths'] = str(sum(c["deaths"] for c in json_response))
                    stats['state'] = json_response[0]["state"]

                    return stats
                elif (len(json_response) == 1):
                    stats = json_response[0]
                    stats['code'] = response.status_code
                    stats['had_data'] = True
                    return stats
        except Exception:
            print("Decsis region exception")
            return {}


class ActionSearchStatsRegion(Action):

    def name(self) -> Text:
        return "action_search_stats_region"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entity = next((e for e in tracker.latest_message["entities"] if
                       e['entity'] == 'country_district' or e['entity'] == 'country_state'), None)
        if entity['entity'] == "country_state":
            description = "state"
        else:
            description = "district"
        region = entity['value']
        print("{} is {}".format(description, region))

        # date = tracker.get_slot("date")
        decsis_api = DecsisAPI()
        stats = decsis_api.search(description, region)

        if stats is None:
            print("3 None")
            return [SlotSet('region_search_successful', 'not-ok'),
                    SlotSet('country_code', 'DE'),
                    FollowupAction('utter_region_nodata'), ]
        elif stats['code'] == 200 and not stats['has_data']:
            print("1", stats['has_data'])
            return [SlotSet('region_search_successful', 'empty'),
                    SlotSet('region', region),
                    SlotSet('country_code', 'DE'),
                    FollowupAction('utter_region_nodata'), ]
        elif stats['code'] == 200 and stats['has_data']:
            print("2", stats['has_data'])
            return [SlotSet('region_search_successful', 'ok'),
                    SlotSet('region', region),
                    SlotSet('region_confirmed_accum', int(stats.get('confirmed_accum', None))),
                    FollowupAction('utter_covid_current_statistics_region'), ]
