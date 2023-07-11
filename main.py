##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import datetime as dt
import smtplib
import random
import pandas as pd

my_email = "sabalethal@gmail.com"
password = "Lethalsaba97"
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
df = pd.read_csv("birthdays.csv")
now = dt.datetime.now()

def happy_birthday(name):
    with open(f"letter_templates/{random.choice(letters)}","r") as file:
        file = file.read()
    file = file.replace("[NAME],",f"{name},")
    return file

for i in range(0, df.shape[0]):
    month = df.iloc[i, 3]
    day = df.iloc[i, 4]
    name = df.iloc[i, 0]
    email = df.iloc[i,1]
    if(now.month == month and now.day == day):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() #secure connection
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="mphosaba1997@gmail.com",
                                msg=f"Subject:Happy Birthday!\n\n{happy_birthday(name)}")
