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