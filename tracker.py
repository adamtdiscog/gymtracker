#! /usr/bin/env python3

import tkinter
import tkinter.font
from tkinter import *
import smtplib
import pygame.mixer
import pygame
import time
import schedule
import datetime
import openpyxl
todays_date = datetime.date.today()
timedelta = datetime.timedelta(days=6)
date1 = todays_date
date2 = date1 - timedelta
day1 = date1.strftime("%d %b %y")
day2 = date2.strftime("%d %b %y")

root = tkinter.Tk()
# root.geometry("1900x1900")
root.wm_attributes('-alpha', '0.0')
root.wm_attributes('-fullscreen', True)
# root.mainloop()
filename = PhotoImage(file="/home/pi/gymtracker/Assets/gym9.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0)
root.title("Awesome Gym Counter")
# root.config(cursor="none")
myFont = tkinter.font.Font(family='Helvetica', size=48, weight='bold')

def email():
    ## Insert email address you would like to mail from
    fromaddr = 'email@email.com'
    ## Insert email address you would like to send to
    toaddrs = ['email@email.com']
    SUBJECT = "Totals for " + str(day2) + " -- " + str(day1)
    TEXT = ','.join(["AD #'s-" + str(ad.get()) + '\n' + "Civ #'s-" + str(civ.get())
            + '\n' + "Ret #'s -" + str(ret.get())])
    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    ## Credentials (if needed)
    ## I used gmail so setup below is for gmail
    ## Enter use name
    username = 'username'
    ## Enter password for email account
    password = 'password'
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    print('Email Sent!')
    print(datetime.datetime.now())

    ad.set(ad.get() * 0)
    civ.set(civ.get() * 0)
    ret.set(ret.get() * 0)


pygame.mixer.init()
pygame.init()

# Menu bar##
menubar = Menu(root)
filemenu = Menu(menubar, relief=FLAT, font=myFont, tearoff=0)
filemenu.add_command(label="E-Mail", command=email)
filemenu.add_command(label="Quit", command=root.destroy)
menubar.add_cascade(label='Admin', menu=filemenu)

# Display MenuBar##
root.config(menu=menubar)
ad = tkinter.IntVar()  # AD
civ = tkinter.IntVar()  # CIV
ret = tkinter.IntVar()  # RET

wb = openpyxl.load_workbook('/home/pi/gymtracker/Assets/counter-3.xlsx')
sheet = wb.active

# AD##
def onClick_ad(event=None):
    ad.set(ad.get() + 1)
    print("AD #'s-" + str(ad.get()))
    sheet['b2'] = str(ad.get())
    wb.save('/home/pi/gymtracker/Assets/counter-3.xlsx')
    pygame.mixer.music.load("/home/pi/gymtracker/Assets/Whistle-noise.mp3")
    pygame.mixer.music.play(0)

# Civ##
def onClick_civ(event=None):
    civ.set(civ.get() + 1)
    print("Civilian #'s-" + str(civ.get()))
    sheet['b3'] = str(civ.get())
    wb.save('/home/pi/gymtracker/Assets/counter-3.xlsx')
    pygame.mixer.music.load("/home/pi/gymtracker/Assets/Retro.mp3")
    pygame.mixer.music.play(0)

# Retired##
def onClick_ret(event=None):
    ret.set(ret.get() + 1)
    print("Retired #'s-" + str(ret.get()))
    sheet['b4'] = str(ret.get())
    wb.save('/home/pi/gymtracker/Assets/counter-3.xlsx')
    pygame.mixer.music.load("/home/pi/gymtracker/Assets/Wrong-number.mp3")
    pygame.mixer.music.play(0)


# AD##

tkinter.Button(root, textvariable=ad, command=onClick_ad, font=myFont, bg = '#003B74', fg='white', relief=FLAT, bd = 0, highlightthickness = 0, highlightcolor = "#003B74", cursor = "none", activeforeground = 'white', activebackground = '#003B74', height = 1, width = 3 ).place(x=100, y=925)

# Civilian##
tkinter.Button(root, textvariable=civ, command=onClick_civ, font=myFont, bg = '#328400', fg='white', relief=FLAT, bd = 0, highlightthickness = 0, highlightcolor = "#328400", cursor = "none", activeforeground = 'white', activebackground = '#328400', height = 1, width = 3 ).place(x=747, y=925)

# Retired##
tkinter.Button(root, textvariable=ret, command=onClick_ret, font=myFont, bg = '#A00004', fg='white', relief=FLAT, bd = 0, highlightthickness = 0, highlightcolor = "#A00004", cursor = "none", activeforeground = 'white', activebackground = '#A00004', height = 1, width = 3 ).place(x=1370, y=925)





mainloop()