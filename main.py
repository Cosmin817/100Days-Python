##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# Done

import smtplib
import datetime as dt
import random
import pandas as pd

my_email = 'cch391.test.email@gmail.com'
password = 'jklpuyrkoogfrwcx'
now = dt.datetime.now()
current_day_of_month = now.day
current_month = now.month
current_birthdays = []
random_letter_number = random.randint(1, 3)
string_message_to_send = ""

# 2. Check if today matches a birthday in the birthdays.csv

birthdays_df = pd.read_csv('birthdays.csv')
birthdays_list = birthdays_df.values.tolist()

for i in birthdays_list:
    if i[3] == current_month and i[4] == current_day_of_month:
        current_birthdays += [i]


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

if len(current_birthdays) > 0:
    for person in current_birthdays:
        string_message_to_send = ""
        with open(f'./letter_templates/letter_{random_letter_number}.txt', 'r') as letter_to_send:
            letter_lines = letter_to_send.readlines()

        for line in letter_lines:
            string_message_to_send += line.replace("[NAME]", f"{person[0]}")

    # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com:587") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=person[1],
                msg=f"Subject:Happy Birthday !\n\n{string_message_to_send}."
            )

