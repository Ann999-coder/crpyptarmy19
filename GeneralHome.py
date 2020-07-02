from tkinter import Toplevel, Button, Tk, Menu
from GeneralPasswordChange import *
from GeneralProfileView import *
from GeneralProfileView import *
from GeneralSecretInformationSend import *
from GeneralViewReport import *
class general():
    def __init__(self, master):

        #top = Tk()
        master.title("General Home")
        master.state("zoomed")
        menubar = Menu(master)
        file = Menu(menubar, tearoff=0)

        file.add_command(label="View Profile", command = self.generalprofileview)
        file.add_command(label="Change password", command = self.generalpasschange)

        file.add_separator()

        file.add_command(label="Exit", command=master.destroy)

        menubar.add_cascade(label="Personal", menu=file)

        edit = Menu(menubar, tearoff=0)

        edit.add_command(label="Report Information", command = self.generalsecretinfosend)
        edit.add_command(label="General View Information", command = self.generalsecretinfoview)
        #edit.add_command(label="View PEID Graph", command=self.peidgraph)

        menubar.add_cascade(label="Activities", menu=edit)
        help = Menu(menubar, tearoff=0)
        help.add_command(label="About")

        menubar.add_cascade(label="Help", menu=help)

        master.config(menu=menubar)

    def generalpasschange(self):
        print("clicked")
        window = Tk()
        self.app = GeneralChangePasswordClass(window)
    def generalprofileview(self):
        print("clicked")
        window = Tk()
        self.app = GeneralProfileViewClass(window)
    def generalsecretinfosend(self):
        print("clicked")
        window = Tk()
        self.app = GeneralSecretInformationSendClass(window)
    def generalsecretinfoview(self):
        print("clicked")
        window = Tk()
        self.app = GeneralViewReportClass(window)

    """def peidgraph(self):
        print("graph clicked...")"""



#top.mainloop()

#root = Tk()



#cls = general(root)

#root.mainloop()
