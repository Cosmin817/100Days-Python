import requests
from twilio.rest import Client

# API_KEY = 60d493d6ce420dbce39c89bc364888bc
# https://api.openweathermap.org/data/2.5/onecall?lat=44.426765&lon=26.102537&exclude=current,minutely,daily,alerts&appid=60d493d6ce420dbce39c89bc364888bc

API_KEY = "60d493d6ce420dbce39c89bc364888bc"
LAT = 49.487457
LON = 8.466040
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "ACb3ecdfb36ca582b3888fb1a11c62af5f"
auth_token = "6274fd2ca9387f41703d443bfa41d6f0"

weather_params = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "exclude": 'current,minutely,daily,alerts'
}

my_request = requests.get(OWM_ENDPOINT, params=weather_params)
my_request.raise_for_status()
my_request_data = my_request.json()

list_of_codes_12h = [hour['weather'][0]['id'] for hour in my_request_data['hourly'][:12]]

if list_of_codes_12h[0] < 700:
    message_bring_umbrella = "It's going to rain today. Remember to bring an ☂️"
    print(message_bring_umbrella)

    client = Client(account_sid, auth_token)

    message = client.messages.create(
      from_='+15673722701',
      body=message_bring_umbrella,
      to='+40749153818'
    )

    print(message.status)