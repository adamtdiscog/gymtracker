#! /usr/bin/env python3

import schedule
import time
import datetime
import openpyxl
todays_date = datetime.date.today()
timedelta = datetime.timedelta(days=6)
date1 = todays_date
date2 = date1 + timedelta
day1 = date1.strftime("%d %b %y")
day2 = date2.strftime("%d %b %y")


wb = openpyxl.load_workbook('/home/pi/gymtracker/Assets/counter-3.xlsx')
wb.create_sheet(index=0, title=str(day1) + " -- " + str(day2))
sheet = wb.active
sheet['b1'] = "Total Count"
sheet['a2'] = "AD/RES"
sheet['a3'] = "Civ"
sheet['a4'] = "Ret"

wb.save('/home/pi/gymtracker/Assets/counter-3.xlsx')