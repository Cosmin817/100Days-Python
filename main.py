# import smtplib
#
# my_email = 'cch391.test.email@gmail.com'
# password = 'jklpuyrkoogfrwcx'
#
# with smtplib.SMTP("smtp.gmail.com:587") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="cch392.test@yahoo.com",
#         msg="Subject:Hello\n\nThis is the Body of my email.")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12,day=15, hour=4)
# print(date_of_birth)

import smtplib
import datetime as dt
import random

my_email = 'cch391.test.email@gmail.com'
password = 'jklpuyrkoogfrwcx'
now = dt.datetime.now()
day_of_week = now.weekday()

with open('quotes.txt', 'r') as quotes:
    all_quotes = quotes.readlines()

random_quote = all_quotes[random.randint(0, len(all_quotes)-1)]

if day_of_week == 1:
    with smtplib.SMTP("smtp.gmail.com:587") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="cch392.test@yahoo.com",
            msg=f"Subject:Inspirational Quote\n\n{random_quote}."
        )
