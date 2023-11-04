import requests
import datetime
from requests.auth import HTTPBasicAuth

# lehaj82825@rdluxe.com
# rdluxe/rdluxe
# Application Key = 353135530ab6b7f0283a37bd19609d58
# Application ID = 052144b1
# POST https://trackapi.nutritionix.com/v2/natural/exercise
# Basic Y2NoOmNjaA==

APP_ID = "052144b1"
API_KEY = "353135530ab6b7f0283a37bd19609d58"

auth_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0'
}

user_query = str(input('Tell me which exercises you did: '))

query = {
 "query": user_query,
 "gender": "male",
 "weight_kg": 71,
 "height_cm": 170,
 "age": 25
}

exercise_info_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
exercise_info_response = requests.post(url=exercise_info_endpoint, headers=auth_headers, json=query)
print(exercise_info_response.json())
exercise_info_response_json = exercise_info_response.json()


for exercise in exercise_info_response_json['exercises']:
    date = datetime.datetime.now().strftime('%d/%m/%Y')
    time = datetime.datetime.now().strftime('%X')
    name = exercise['name'].title()
    duration = exercise['duration_min']
    calories = exercise['nf_calories']

    add_row_endpoint = 'https://api.sheety.co/6bd7cb43b31c572c80b4d9378a3f3767/workoutTracking/workouts'
    body = {
      "workout": {
        'date': date,
        'time': time,
        'exercise': name,
        'duration': duration,
        'calories': calories
      }
    }

    basic = HTTPBasicAuth('cch', 'cch')
    add_row_response = requests.post(
                                         url=add_row_endpoint,
                                         json=body,
                                         auth=basic,
                                         headers={
                                             "Content-Type": "application/json"
                                                }
                                     )

    print(add_row_response)


