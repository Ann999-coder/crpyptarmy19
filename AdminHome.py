from tkinter import Toplevel, Button, Tk, Menu
from AdminChangePassword import AdminPasswordChangeClass
from AddNewOfficer import *
from RemoveOfficer import *
from IDBasedSerch import *
from AdminRankBasedSearch import *
from ListAllOfficers import *
from myprofile import *

class adminhome():
    def __init__(self, master):
        #top = Tk()
        master.title("Admin Home")
        master.state("zoomed")
        menubar = Menu(master)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="my profile",command = self.showmyprofile)

        file.add_command(label="New Officer Appointment",command = self.showaddnewuser)
        file.add_command(label="Remove Officer", command = self.showremoveofficer)


        file.add_command(label="Change Password",command = self.showchangepassword)
        file.add_separator()
        file.add_command(label="Logout" ,command=master.destroy)

        menubar.add_cascade(label="Activites", menu=file)
        edit = Menu(menubar, tearoff=0)
        edit.add_command(label="IDBased", command = self.idbased)

        edit.add_command(label="Rank Based", command = self.rankbased)
        edit.add_separator()

        edit.add_command(label="Select All Officers",command = self.listallofficers)

        menubar.add_cascade(label="LogReport", menu=edit)
        help = Menu(menubar, tearoff=0)
        help.add_command(label="About")
        menubar.add_cascade(label="Help", menu=help)

        master.config(menu=menubar)
    def showmyprofile(self):
        print("clicked")
        window = Tk()
        self.app = MyprofileClass(window)

    def showchangepassword(self):
        print("clicked")
        window = Tk()
        self.app = AdminPasswordChangeClass(window)

    def showaddnewuser(self):
        print("clicked")
        window = Tk()
        self.app = AddNewOfficerClass(window)
    def showremoveofficer(self):
        print("clicked")
        window = Tk()
        self.app = RemoveOfficerClass(window)
    def idbased(self):
        print("clicked")
        window = Tk()
        self.app = AdminIDBasedSearchClass(window)
    def rankbased(self):
        print("clicked")
        window = Tk()
        self.app = RankBasedSearchClass(window)
    def listallofficers(self):
        print("clicked")
        window = Tk()
        self.app = ListAllOfficersClass(window)


#top.mainloop()
