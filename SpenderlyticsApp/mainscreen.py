import tkinter as tk
from tkinter import *
from mypart import *
from pdfgenerator import *
from PIL import ImageTk, Image
def createscreen():
    mainscreen = tk.Tk()
    mainscreen.title("Spenderlytics")
    mainscreen.configure(background="Black")
    mainscreen.geometry("400x400")
    mainscreen.wm_iconphoto(False, ImageTk.PhotoImage(Image.open('Spenderlyticslogoicon.png')))

    bg = ImageTk.PhotoImage(file="SpenderlyticsLogo.png")
    canvas = Canvas(mainscreen, width=400, height=400)
    canvas.pack(fill=BOTH, expand=True)
    canvas.create_image(0, 0, image=bg, anchor='nw')

    button1 = tk.Button(mainscreen, text = "Top 25% LTV Customers Contribution to Total Spend", activebackground="lightgreen",width=45,height=1,command=generatefigure1)
    button1.place(x=40,y=130)

    button2 = tk.Button(mainscreen, text = "Prophet Forecast for Top 25% LTV Customers Total Spend", activebackground="lightgreen",width=45,height=1,command=generatefigure2)
    button2.place(x=40,y=160)

    button3 = tk.Button(mainscreen, text = "ARIMA Forecast for Top 25% TLV Customers Total Spend", activebackground="lightgreen",width=45,height=1,command=generatefigure3)
    button3.place(x=40,y=190)

    button4 = tk.Button(mainscreen, text = "Generate PDF", activebackground="lightgreen",width=10,height=1,command=generatepdf)
    button4.place(x=165,y=220)

    def resize_image(e):
        global image, resized, image2
        # open image to resize it
        image = Image.open("SpenderlyticsLogo.png")
        # resize the image with width and height of root
        resized = image.resize((e.width, e.height))

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

    mainscreen.bind("<Configure>", resize_image)