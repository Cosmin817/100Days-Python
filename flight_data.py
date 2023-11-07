# This FlightData class is responsible for structuring the flight data.
#https://tequila.kiwi.com/
    #API_KEY=r49LGTYaqj2zLXDI2Jctu4KVCumc95S
    #AffilID=cosmincmcflightsearch
import requests

# curl -X 'GET' \
#   'https://api.tequila.kiwi.com/locations/query?term=Paris&locale=en-US&location_types=city&limit=1&active_only=true' \
#   -H 'accept: application/json' \
#   -H 'apikey: _r49LGTYaqj2zLXDI2Jctu4KVCumc95S'

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "_r49LGTYaqj2zLXDI2Jctu4KVCumc95S"

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
        params = {
            'fly_from': city_from,
            'fly_to': city_destination,
            'date_from': '08/11/2023',
            'date_to': '06/05/2024',
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
            # 'selected_cabins': 'C',
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
            'limit': '500',
            'sort': 'price'
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=self.header, params=params)
        print(response.json()['data'][0]['price']) # price to destination
        print(len(response.json()['data']))
        pass

test_object = FlightData()
test_object.get_flight('BUH','BER')