from tkinter.ttk import *
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import os

class ViewAboutClass:
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
        top.geometry("350x450")
        top.configure(bg="white")


        top.title("")



        text=Text(top,bg="white")
        text.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        text.insert(INSERT,"About Us\n")
        text.insert(INSERT, "The Indian Army is the land-based branch and the largest component of the Indian Armed Forces.The President of India is the Supreme Commander of the  and its professional head is the Chief of Army Staff (COAS), who is a four-star general.In this system Perceptual image encryption provides an efﬁcient and effective way to preserve the conﬁdentiality of visual information,and the measurement of content leakage is of fundamental importance for perceptually encrypted images.The System is used to securely send confidential images in an encrypted form in military application")
        text.pack()



        top.mainloop()

#top = Tk()
#cp = ViewAboutClass(top)
#top.mainloop()

