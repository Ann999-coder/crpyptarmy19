from tkinter import Toplevel, Button, Tk, Menu
from ColonelChangePassword import *
from ColonelProfileView import *
from ColonelSecretInformationSend import *
from ColonelViewReport import *
class colonel():
    def __init__(self, master):

        #top = Tk()
        master.title("Colonel Home")
        master.state("zoomed")
        menubar = Menu(master)
        file = Menu(menubar, tearoff=0)

        file.add_command(label="View Profile", command = self.colonelprofilelist)
        file.add_command(label="Change password", command = self.colonelpasschange)

        file.add_separator()

        file.add_command(label="Exit", command=master.destroy)

        menubar.add_cascade(label="Personal", menu=file)

        edit = Menu(menubar, tearoff=0)

        edit.add_command(label="Report Information", command = self.colonelreportsend)
        edit.add_command(label="View Information Report", command = self.colonelreportview)

        menubar.add_cascade(label="Activities", menu=edit)
        help = Menu(menubar, tearoff=0)
        help.add_command(label="About")

        menubar.add_cascade(label="Help", menu=help)

        master.config(menu=menubar)

    def colonelpasschange(self):
        print("clicked")
        window = Tk()
        self.app = ColonelChangePasswordClass(window)
    def colonelprofilelist(self):
        print("clicked")
        window = Tk()
        self.app = ColonelProfileViewClass(window)
    def colonelreportsend(self):
        print("clicked")
        window = Tk()
        self.app = ColonelSecretInformationSendClass(window)
    def colonelreportview(self):
        print("clicked")
        window = Tk()
        self.app = ColonelViewReportClass(window)

#top.mainloop()

#root = Tk()

# root.title("Login")

#root.geometry("375x250")

#cls = colonel(root)

#root.mainloop()
