# https://requests.readthedocs.io/en/latest/api/
# https://docs.pixe.la/
# https://pixe.la/

import requests
from datetime import datetime

# USERNAME = "zed"
# TOKEN = "mamaliga_goala_haha"

# pixela_endpoint = "https://pixe.la/v1/users"
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=f"{pixela_endpoint}", json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
#
# today = datetime.now()
# print(today)
# print(today.strftime("%Y%m%d"))

# pixel_config = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "100"
#  }

# headers = {
#      "X-USER-TOKEN": TOKEN
#  }
#
# response = requests.post(url=graph_endpoint, json=pixel_config, headers=headers)

USERNAME = "zed"
GRAPHID = "graph1"
today = datetime.now()
update_string = today.strftime("%Y%m%d")
endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/{update_string}"
TOKEN = "mamaliga_goala_haha"

headers = {
      "X-USER-TOKEN": TOKEN
}

pixel_config = {
    "quantity": "400"
 }

response = requests.put(url=endpoint, json=pixel_config, headers=headers)
print(response)
print(update_string)

