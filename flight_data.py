# This FlightData class is responsible for structuring the flight data.
#https://tequila.kiwi.com/
    #API_KEY=r49LGTYaqj2zLXDI2Jctu4KVCumc95S
    #AffilID=cosmincmcflightsearch
import requests
from datetime import datetime, timedelta

# curl -X 'GET' \
#   'https://api.tequila.kiwi.com/locations/query?term=Paris&locale=en-US&location_types=city&limit=1&active_only=true' \
#   -H 'accept: application/json' \
#   -H 'apikey: _r49LGTYaqj2zLXDI2Jctu4KVCumc95S'

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "_r49LGTYaqj2zLXDI2Jctu4KVCumc95S"
FUTURE_DATE_AFTER_1DAY = (datetime.now() + timedelta(days=1)).strftime('%d/%m/%Y')
FUTURE_DATE_AFTER_6MONTHS = (datetime.now() + timedelta(days=180)).strftime('%d/%m/%Y')


class FlightData:
    def __init__(self):
        self.header = {
            'accept': 'application/json',
            'apikey': f'{TEQUILA_API_KEY}'
        }

    def get_city_iata_code(self, city: str) -> str:
        params = {
            'term': city,
            # 'term': 'Paris',
            'locale': 'en-US',
            'location_types': 'city',
            'limit': '1',
            'active_only': 'true'
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=self.header, params=params)
        city_iana_code = response.json()['locations'][0]['code']
        output = city_iana_code
        return output

    def get_flight(self, city_from, city_destination):
        output = {}
        params = {
            'fly_from': city_from,
            'fly_to': city_destination,
            'date_from': FUTURE_DATE_AFTER_1DAY,
            'date_to': FUTURE_DATE_AFTER_6MONTHS,
            # 'return_from': '04/04/2021',
            # 'return_to': '06/04/2021',
            'nights_in_dst_from': '7',
            'nights_in_dst_to': '28',
            'max_fly_duration': '20',
            'ret_from_diff_city': 'false',
            'ret_to_diff_city': 'false',
            'one_for_city': '0',
            'one_per_date': '0',
            'adults': '1',
            # 'children': '2',
            # 'selected_cabins': 'M',
            # 'mix_with_cabins': 'M',
            'adult_hold_bag': '1',
            'adult_hand_bag': '1',
            # 'child_hold_bag': '2,1',
            # 'child_hand_bag': '1,1',
            'only_working_days': 'false',
            'only_weekends': 'false',
            'partner_market': 'eu',
            'max_stopovers': '0',
            'max_sector_stopovers': '0',
            'vehicle_type': 'aircraft',
            'limit': '200',
            'sort': 'price' # sort after the price, the smallest price is at index 0
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=self.header, params=params)
        try:
            output['lowest_price_flight'] = float(response.json()['data'][0]['price']) # price to destination
            output['city_from'] = str(response.json()['data'][0]['cityFrom'])
            output['airpot_iata_code_from'] = str(response.json()['data'][0]['flyFrom'])
            output['city_to'] = str(response.json()['data'][0]['cityTo'])
            output['airpot_iata_code_to'] = str(response.json()['data'][0]['flyTo'])
            output['outbound_date'] = str(response.json()['data'][0]['local_departure']).split("T")[0]
            output['inbound_date'] = str(response.json()['data'][0]['route'][1]['local_departure']).split("T")[0]
            return output
        except IndexError:
            return "None"