from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter.ttk import Button
from base64_background import base64_background
from base64_btclogo import base64_btc
from base64_qlclogo import base64_qlc
from base64_powrlogo import base64_powr
import requests
import base64

root = Tk()
root.title("Binance Exchange Asset Prices")
url = "https://api.binance.com/api/v1/ticker/price"

# Adds blank space between buttons and prices
Label(root, text="   ").grid(rowspan=3, column=3)

# Adds background image to widget
base64_background = base64.b64decode(base64_background)
background_image = PhotoImage(data=base64_background)
background_smaller_image = background_image.subsample(7, 7)
background_label = Label(root, image=background_smaller_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Asset API requests and display
def BTCprice_refresh():
    querystring = {"symbol": "BTCUSDT"}
    response = requests.request("GET", url, params=querystring)
    print(response.text)
    BTClabel.set("$" + response.text[-16:-2])
    root.command(btn1)

def QLCprice_refresh():
    querystring = {"symbol": "QLCBTC"}
    response = requests.request("GET", url, params=querystring)
    print(response.text)
    QLClabel.set("BTC" + response.text[-12:-2])
    root.command(btn2)

def POWRprice_refresh():
    querystring = {"symbol": "POWRBTC"}
    response = requests.request("GET", url, params=querystring)
    print(response.text)
    POWRlabel.set("BTC" + response.text[-12:-2])
    root.command(btn3)

# Refreshes labels without repeating
BTClabel = StringVar()
QLClabel = StringVar()
POWRlabel = StringVar()
BTClabel.set("")
QLClabel.set("")
POWRlabel.set("")

# Label information
Label(root, textvariable=BTClabel, font=("Arial Bold", 16), height=2, width=18, borderwidth=5, relief="ridge", padx=3, pady=3).grid(row=1, column=4, padx=(10, 30), pady=(10, 3))
Label(root, textvariable=QLClabel, font=("Arial Bold", 16), height=2, width=18, borderwidth=5, relief="ridge", padx=3, pady=3).grid(row=2, column=4, padx=(10, 30), pady=(4,0))
Label(root, textvariable=POWRlabel, font=("Arial Bold", 16), height=2, width=18, borderwidth=5, relief="ridge", padx=3, pady=3).grid(row=3, column=4, padx=(10, 30), pady=(3, 10))

# BTC button photo
base64_btc = base64.b64decode(base64_btc)
btc_image = PhotoImage(data=base64_btc)
btc_smaller_image = btc_image.subsample(20, 20)

# QLC button photo
base64_qlc = base64.b64decode(base64_qlc)
qlc_image = PhotoImage(data=base64_qlc)
qlc_smaller_image = qlc_image.subsample(13, 13)

# POWR button photo
base64_powr = base64.b64decode(base64_powr)
powr_image = PhotoImage(data=base64_powr)
powr_smaller_image = powr_image.subsample(5, 5)

# BTC button location and function
btn1 = Button(root, text="BTC Price", image=btc_smaller_image, command=BTCprice_refresh)
btn1.grid(row=1, column=1, padx=10, pady=(10, 0))
btn1.configure(image=btc_smaller_image, compound=RIGHT)

# QLC button location and function
btn2 = Button(root, text="QLC Price", image=qlc_smaller_image, command=QLCprice_refresh)
btn2.grid(row=2, column=1, padx=10, pady=(5,0))
btn2.configure(image=qlc_smaller_image, pad=5, compound=RIGHT)

# POWR button location and function
btn3 = Button(root, text="POWR Price", image=powr_smaller_image, command=POWRprice_refresh)
btn3.grid(row=3, column=1, padx=10, pady=(6,10))
btn3.configure(image=powr_smaller_image, pad=5, compound=RIGHT)

# Asset API functions upon opening widget
BTCprice_refresh(), QLCprice_refresh(), POWRprice_refresh()

root.resizable(width=False, height=False)
root.mainloop()

