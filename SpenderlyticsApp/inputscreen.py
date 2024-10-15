import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import *
from PIL import ImageTk, Image
from importdatafile import importdata
from mainscreen import createscreen
from mycalcs import mycalc
def getfile():
    path = askopenfilename()
    importdata(path)
    mycalc()
    inputscreen.destroy()
    createscreen()

inputscreen = tk.Tk()
inputscreen.title("Spenderlytics")
inputscreen.configure(background="Black")
inputscreen.geometry("300x300")
inputscreen.wm_iconphoto(False, ImageTk.PhotoImage(Image.open('Spenderlyticslogoicon.png')))

bg = ImageTk.PhotoImage(file="SpenderlyticsLogo.png")
canvas = Canvas(inputscreen, width=300, height=300)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg, anchor='nw')

inputbutton = tk.Button(inputscreen, text = "Upload File", activebackground="lightgreen",width=10,height=1,command=getfile)
inputbutton.place(x=110,y=120)

inputscreenlabel = tk.Label(inputscreen, text = "Click the button to upload data file.",width=30,height=1)
inputscreenlabel.place(x=45,y=80)

def resize_image(e):
   global image, resized, image2
   # open image to resize it
   image = Image.open("SpenderlyticsLogo.png")
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height))

   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor='nw')

inputscreen.bind("<Configure>", resize_image)
inputscreen.mainloop()