import datetime as dt
import pandas
import random
import smtplib

PLACEHOLDER = "[NAME]"
EMAIL = "shubh.python.test@gmail.com"
PASSWORD = "yzkdciszgiwgfdum"
# estpdswrd "tpython474"
PORT = 587

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
# HINT 2: Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")
month = data["month"][0]
day = data["day"][0]

now = dt.datetime.now()
today_month = now.month
today_day = now.day
print(today_day)
print(today_month)
if month == today_month and day == today_day:
    letter_choice = random.choice(letters)
    with open(f"./letter_templates/{letter_choice}") as template:
        template_content = template.read()
        letter = template_content.replace(PLACEHOLDER, "Mommy")

        with smtplib.SMTP("smtp.gmail.com", PORT) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(to_addrs="mickeyjoshdecember@gmail.com", from_addr=EMAIL,
                                msg=f"Subject: Automated Birthday Wishes\n\n{letter}")

