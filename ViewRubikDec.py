from tkinter.ttk import *
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os

class ViewRubikDecClass:
    def __init__(self, top):

        large_font = ('Verdana', 14)
        large_font2 = ('Verdana', 14)
        lab1 = ('Verdana', 14)
        lab2 = ('Verdana', 14)
        bt_size = ('Verdana', 14)


        fpath = StringVar()
        self.top=top

        windowWidth = top.winfo_reqwidth()
        windowHeight = top.winfo_reqheight()
        print("Width", windowWidth, "Height", windowHeight)

        positionRight = int(top.winfo_screenwidth() / 7 - windowWidth / 2)
        positionDown = int(top.winfo_screenheight() / 7 - windowHeight / 2)

        # Positions the window in the center of the page.
        top.geometry("+{}+{}".format(positionRight, positionDown))
        # top.geometry("+{}+{}".format(600, 250))
        top.geometry("900x650")


        top.title("")
        self.viewrubik()
    def viewrubik(self):
        canvas = Canvas(self.top, width="950", height="500")  # .place(x=20, y=210)
        decr_img = os.getcwd() + "\\" + "Decryption" + "\\" + "rubik.png"
        filename = decr_img

        img = PhotoImage(file=filename)
        canvas.create_image(0, 0, image=img, anchor=NW)

        canvas.pack()
        canvas.place(x=20, y=170)
        mainloop()



#top = Tk()

#cp = ViewRubikEncClass(top)
#top.mainloop()

