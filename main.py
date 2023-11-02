# https://requests.readthedocs.io/en/latest/api/
# https://docs.pixe.la/
# https://pixe.la/

import requests

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "mamaliga_goala_haha",
    "username": "zed",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=f"{pixela_endpoint}", json=user_params)
# print(response.text)

