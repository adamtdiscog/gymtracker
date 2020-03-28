#! /usr/bin/env python3
import yagmail
# from counter_backup.py import tdip
import datetime
todays_date = datetime.date.today()
timedelta = datetime.timedelta(days=6)
date1 = todays_date
date2 = date1 - timedelta
day1 = date1.strftime("%d %b %y")
day2 = date2.strftime("%d %b %y")

## Enter email sending from and login password **Note:yagmail is a GMAIL/SMTP client that aims to make it as simple as possible to send emails.
yag = yagmail.SMTP("user@gmail.com", "password")

## Enter email address sending to & message/attachments
yag.send(to=['user@email.com'], subject="Totals for " + str(day2) + " -- " + str(day1), contents= "Please see attached for weekly totals.", attachments="/home/pi/gymtracker/gymtracker/Assets/counter-3.xlsx")