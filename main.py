import requests
from datetime import datetime
import smtplib
from config import *
import time

MY_LAT = 44.426765  # Your latitude
MY_LONG = 26.102537  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
time_now_hour = int(time_now.strftime('%H'))


# If the ISS is close to my current position and it is currently dark
# if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (sunrise <= time_now_hour <= sunset):

while True:
    if (MY_LAT - 5 <= MY_LAT <= MY_LAT + 5) and (sunrise <= time_now_hour <= sunset):
        # Then send me an email to tell me to look up.
        with smtplib.SMTP("smtp.gmail.com:587") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=person,
                msg=f"Subject:ISS Alert !\n\n{string_message_to_send}."
            )
        print('I just sent an email using Python smtplib')
        print(f'{iss_latitude} {iss_longitude}')
    time.sleep(60)


# BONUS: run the code every 60 seconds.



