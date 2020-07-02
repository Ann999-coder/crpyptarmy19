from tkinter import Toplevel, Button, Tk, Menu
from MajorGeneralPasswordChange import *
from MajorGeneralProfileView import *
from MajorSecretInformationSend import *
from MajorGeneralViewReport import *
class majorgeneral():
    def __init__(self, master):

        #top = Tk()
        master.title("Major General Home")
        master.state("zoomed")
        menubar = Menu(master)
        file = Menu(menubar, tearoff=0)

        file.add_command(label="View Profile", command = self.majorprofileview)
        file.add_command(label="Change password", command = self.majorpasschange)

        file.add_separator()

        file.add_command(label="Exit", command=master.destroy)

        menubar.add_cascade(label="Personal", menu=file)

        edit = Menu(menubar, tearoff=0)

        edit.add_command(label="Report Information", command = self.majorsecretinfosend)
        edit.add_command(label="Major General View Information", command = self.majorsecretinfoview)

        menubar.add_cascade(label="Activities", menu=edit)
        help = Menu(menubar, tearoff=0)
        help.add_command(label="About")

        menubar.add_cascade(label="Help", menu=help)

        master.config(menu=menubar)

    def majorpasschange(self):
        print("clicked")
        window = Tk()
        self.app = MajorGeneralChangePasswordClass(window)
    def majorprofileview(self):
        print("clicked")
        window = Tk()
        self.app =MajorGeneralProfileViewClass(window)
    def majorsecretinfosend(self):
        print("clicked")
        window = Tk()
        self.app = MajorSecretInformationSendClass(window)
    def majorsecretinfoview(self):
        print("clicked")
        window = Tk()
        self.app = MajorGeneralViewReportClass(window)

#top.mainloop()

#root = Tk()

# root.title("Login")

#root.geometry("375x250")

#cls = colonel(root)

#root.mainloop()
