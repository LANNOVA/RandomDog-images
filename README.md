# RandomDog-images



## API

URL of the API - https://dog.ceo/dog-api/

API - https://dog.ceo/api/breeds/image/random/

 ### JSON
```json

{
    "message": "https://images.dog.ceo/breeds/kelpie/n02105412_2631.jpg",
    "status": "success"
}

```
## CODE

### Imported Things

```py
import tkinter as tk 
import requests #required for api
from tkinter import *
from PIL import ImageTk,Image #for image
from urllib.request import urlopen #for using image as url
import os #os
import urllib.request #url requeat
import io
from tkinter import Button #button for next option
from io import BytesIO
import asyncio #not required
import datetime #not required

```
### For requesting api and tkinter for use
```py

response=requests.get("https://dog.ceo/api/breeds/image/random")
data= response.json()
root = tk.Tk()
```
### Restart function 
```py
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

Button(root, text="Next", command=restart_program).pack()
```
### adding the image

```py
URL = data["message"]
u = urlopen(URL)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
photo = ImageTk.PhotoImage(im)

label = tk.Label(image=photo)
label.image = photo
label.pack()
 
root.mainloop()

```
## Output
**You can see output in the output.jpeg**


