import requests
SHEETY_ENDPOINT_GET = "https://api.sheety.co/6bd7cb43b31c572c80b4d9378a3f3767/flightDealsCch/prices"
SHEETY_ENDPOINT_POST = "https://api.sheety.co/6bd7cb43b31c572c80b4d9378a3f3767/flightDealsCch/prices"
SHEETY_ENDPOINT_PUT ="https://api.sheety.co/6bd7cb43b31c572c80b4d9378a3f3767/flightDealsCch/prices/"

#This DataManager class is responsible for talking to the Google Sheet.


class DataManager:
    def __init__(self):
        self.get_sheety_endpoint = SHEETY_ENDPOINT_GET
        self.post_sheety_endpoint = SHEETY_ENDPOINT_POST

    def get_sheet_data(self):
        url = self.get_sheety_endpoint
        response = requests.get(url)
        json_response = response.json()
        # temporar_output = [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]
        return json_response['prices']
        # return temporar_output

    def set_city_iata_code(self, rowid, city_iata_code):
        url = f'{SHEETY_ENDPOINT_PUT}/{rowid}'
        body = {
            'price': {
                'iataCode': city_iata_code
            }
        }
        response = requests.put(url, json=body)
        print(response.json())
        return 0

    def get_email_list(self):
        url = 'https://api.sheety.co/6bd7cb43b31c572c80b4d9378a3f3767/flightDealsCch/users'
        response_get_gsheet = requests.get(url)
        data = response_get_gsheet.json()

        emails_list = [email['email'] for email in data['users']]
        return emails_list
