from tkinter import Toplevel, Button, Tk, Menu
from LtColonelPasswordChange import *
from LtColonelProfileView import *
from LtColonelSecretInformationSend import *
from LtColonelViewReport import *
class ltcolonel():
    def __init__(self, master):

        #top = Tk()
        master.title("Lieutenant Colonel Home")
        master.state("zoomed")
        menubar = Menu(master)
        file = Menu(menubar, tearoff=0)

        file.add_command(label="View Profile", command = self.ltcolonelview)
        file.add_command(label="Change password", command = self.ltcolonelpasschange)

        file.add_separator()

        file.add_command(label="Exit", command=master.destroy)

        menubar.add_cascade(label="Personal", menu=file)

        edit = Menu(menubar, tearoff=0)

        edit.add_command(label="Report Information", command = self.ltcolonelreportsend)
        edit.add_command(label="View Information Report", command = self.ltcolonelreportview)

        menubar.add_cascade(label="Activities", menu=edit)
        help = Menu(menubar, tearoff=0)
        help.add_command(label="About")

        menubar.add_cascade(label="Help", menu=help)

        master.config(menu=menubar)
    def ltcolonelpasschange(self):
        print("clicked")
        window = Tk()
        self.app = LtColonelPasswordChangeClass(window)
    def ltcolonelview(self):
        print("clicked")
        window = Tk()
        self.app = LtColonelProfileViewClass(window)
    def ltcolonelreportsend(self):
        print("clicked")
        window = Tk()
        self.app = LtColonelSecretInformationSendClass(window)
    def ltcolonelreportview(self):
        print("clicked")
        window = Tk()
        self.app = LtColonelViewReportClass(window)

#top.mainloop()

#root = Tk()

# root.title("Login")

#root.geometry("375x250")

#cls = ltcolonel(root)

#root.mainloop()
