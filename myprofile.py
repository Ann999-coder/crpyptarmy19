from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk

class MyprofileClass:
    def __init__(self, top):
        large_font = ('Verdana', 15)
        large_font2 = ('Verdana', 15)
        large_font3 = ('Verdana', 15)
        lab1 = ('Verdana', 15)
        lab2 = ('Verdana', 15)
        lab3 = ('Verdana', 15)
        lab4 = ('Verdana', 15)
        lab5 = ('Verdana', 15)
        lab5 = ('Verdana', 12)
        bt_size = ('Verdana', 15)

        #top = Tk()

        windowWidth = top.winfo_reqwidth()
        windowHeight = top.winfo_reqheight()
        print("Width", windowWidth, "Height", windowHeight)

        positionRight = int(top.winfo_screenwidth() / 3 - windowWidth / 2)
        positionDown = int(top.winfo_screenheight() / 3 - windowHeight / 2)

        # Positions the window in the center of the page.
        top.geometry("+{}+{}".format(positionRight, positionDown))
        # top.geometry("+{}+{}".format(600, 250))

        top.geometry("400x400")

        top.title("Admin Profile")
        top.configure(bg="white")

        logo_icon = ImageTk.PhotoImage(file="lg.png")
        # logo_icon= PhotoImage(file="password.png")

        Login_Frame = Frame(top, bg="white")
        Login_Frame.place(x=150, y=10)
        logo_lbl = Label(Login_Frame, image=logo_icon).grid(row=0, column=0, pady=20)

        designation = Label(top, text="Designation :", font=lab1,bg="white").place(x=30, y=230)
        userid = Label(top, text="User Id       :", font=lab2,bg="white").place(x=30, y=290)

        # login = Button(top, text="Remove", font=bt_size).place(x=300, y=450)
        # cancel = Button(top, text = "Cancel",activebackground = "pink", activeforeground = "blue",font=bt_size).place(x = 120, y = 170)
        cancel = Button(top, text="Cancel", font=bt_size, command=top.destroy).place(x=300, y=330)

        e1 = Label(top, text="Admin", font=large_font,bg="white").place(x=170, y=230)
        e2 = Label(top, text="admin", font=large_font,bg="white").place(x=170, y=290)
        top.mainloop()

