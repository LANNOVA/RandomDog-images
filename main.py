import tkinter as tk
import requests
#import urllib2
from tkinter import *
from PIL import ImageTk,Image
from urllib.request import urlopen
import os
import urllib.request
import io
from tkinter import Button
from io import BytesIO
import asyncio
import datetime
response=requests.get("https://dog.ceo/api/breeds/image/random")
data= response.json()
root = tk.Tk()

URL = data["message"]
u = urlopen(URL)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
photo = ImageTk.PhotoImage(im)

label = tk.Label(image=photo)
label.image = photo
label.pack()


def restart_program():
    
    python = sys.executable
    os.execl(python, python, * sys.argv)

Button(root, text="Next", command=restart_program).pack()


  
root.mainloop()


#print(data)
print(data["message"])
