# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import pandas as pd
import datetime as dt
import random
import smtplib
import os

my_email = os.environ.get("my_email")
my_password = os.environ.get("my_password")

data = pd.read_csv("birthdays.csv")

today = dt.datetime.now()
today_day = today.day
today_month = today.month

birthday_matches = data[(data["day"] == today_day) & (data["month"] == today_month)]

if not birthday_matches.empty:
    letter_num = random.randint(1,4)
    with open(f"letter_templates/letter_{letter_num}.txt") as f:
        available_letters = f.read()

    for index, row in birthday_matches.iterrows():
        name = row["name"]
        email = row["email"]
        letter_to_be_sent = available_letters.replace("[NAME]", name)
        letter_to_be_sent = f"Subject: Happy Birthday\n\n{letter_to_be_sent}"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(my_email, email, letter_to_be_sent)
