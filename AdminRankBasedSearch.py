from tkinter.ttk import *
from tkinter import *

class RankBasedSearchClass:
    def __init__(self, top):
        lab2 = ('Verdana', 15)
        bt_size = ('Verdana', 15)
        #top = Tk()
        top.title("Rank Based")

        windowWidth = top.winfo_reqwidth()
        windowHeight = top.winfo_reqheight()
        print("Width", windowWidth, "Height", windowHeight)

        positionRight = int(top.winfo_screenwidth() / 3 - windowWidth / 2)
        positionDown = int(top.winfo_screenheight() / 3 - windowHeight / 2)

        # Positions the window in the center of the page.
        top.geometry("+{}+{}".format(positionRight, positionDown))
        # top.geometry("+{}+{}".format(600, 250))
        top.geometry("450x400")

        top.title("Rank Based Search")

        rank = Label(top, text="Rank", font=lab2).place(x=10, y=30)

        combo = Combobox(top, font=lab2)
        combo['values'] = ("general", "colonel", "Lt.colonel", "MajorGeneral")
        combo.current(3)
        combo.place(x=80, y=30)

        go = Button(top, text="GO", font=bt_size).place(x=390, y=25)
        cancel = Button(top, text="Cancel", font=bt_size, command=top.destroy).place(x=250, y=350)

        listbox = Listbox(top)

        listbox.insert(1, "Name:")

        listbox.insert(2, "DOB:")

        listbox.insert(3, "Address:")

        listbox.insert(4, "city:")

        listbox.insert(5, "Mobile no:")
        listbox.place(x=10, y=90)

        top.mainloop()
