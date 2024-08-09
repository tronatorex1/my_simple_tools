# This tkinter gui shows your current location and Ip address
#   https://www.geeksforgeeks.org/python-tkinter-tutorial/

from tkinter import *
import time as tm
import requests
import json

# variables
ip_addr = country = ""

# create root window
root = Tk()
root.title("TKinter for MyIp/Location")
root.geometry('460x170')

# all widgets will be here
res = requests.get("https://api.myip.com").json()
country = res['country']
ip_addr = res['ip']
lbl1 = Label(root, text = "You Current Ip: " + ip_addr, font="Arial 22", justify="left")
lbl2 = Label(root, text = "You Location: " + country, font="Arial 22", justify="right")
lbl1.pack(pady=5, padx=10, anchor="w")
lbl2.pack(pady=5, padx=10, anchor="w")

def close():
    root.destroy()

def update():
    lbl1.configure(text="+You Current Ip: " + ip_addr, font="Arial 22", justify="left")
    lbl2.configure(text="+You Current Location: " + country, font="Arial 22", justify="left")

button1 = Button(root, text="   Close    ", command=close)
button1.pack(pady=1)

button2 = Button(root, text="  Update  ", command=update)
button2.pack(pady=1)

# Execute Tkinter
root.mainloop()