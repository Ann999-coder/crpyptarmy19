from tkinter.ttk import *
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


large_font = ('Verdana', 14)
large_font2 = ('Verdana', 14)
lab1 = ('Verdana', 14)
lab2 = ('Verdana', 14)
bt_size = ('Verdana', 14)

top = Tk()
fpath = StringVar()

windowWidth = top.winfo_reqwidth()
windowHeight = top.winfo_reqheight()
print("Width", windowWidth, "Height", windowHeight)

positionRight = int(top.winfo_screenwidth() / 7 - windowWidth / 2)
positionDown = int(top.winfo_screenheight() / 7 - windowHeight / 2)

        # Positions the window in the center of the page.
top.geometry("+{}+{}".format(positionRight, positionDown))
        # top.geometry("+{}+{}".format(600, 250))
top.geometry("900x650")

top.title("Major Information Passing")

image = Label(top, text="Image Path", font=("times new roman", 15, "bold")).place(x=10, y=80)

combo1 = Combobox(top)
combo1['values'] = "1"
combo1.place(x=140,y=80)
cancel = Button(top, text="DEC1", font=bt_size,width=5,relief=RIDGE,bg="light gray",command=top.destroy).place(x=770, y=360)
logout = Button(top, text="DEC2", font=bt_size, width=5).place(x=770, y=250)
psswd = Button(top, text="DEC3", font=bt_size, bg="light gray",width=5).place(x=770,y=470)
top.mainloop()
