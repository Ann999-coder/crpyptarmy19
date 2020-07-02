#!/usr/bin/env python
import mysql.connector
from tkinter import *
from home import *
from ColonelHome import *
from GeneralHome import *
from LtColonel import *
from MajorGeneralHome import *
from AdminHome import *
from tkinter import messagebox
from PIL import Image, ImageTk
from myprofile import MyprofileClass
import random
import string
from AdminChangePassword import AdminPasswordChangeClass
from about import ViewAboutClass
from OtpPassword import OtpPasswordClass
import foo
import requests
import json
from PerceptEnc import PerceptualEncClass


URL = 'https://www.sms4india.com/api/v1/sendCampaign'




top = Tk()


uname = StringVar()
upass = StringVar()
USER_TYPE=StringVar()
#--------------------------------------------------------------

def ltcolonelpasschange():
    print("clicked")
    window = Toplevel()
    app = LtColonelPasswordChangeClass(window)


def ltcolonelview():
    print("clicked")
    window = Toplevel()
    app = LtColonelProfileViewClass(window)


def ltcolonelreportsend():
    print("clicked")
    window = Toplevel()
    app = LtColonelSecretInformationSendClass(window)


def ltcolonelreportview():
    print("clicked")
    window = Toplevel()
    app = LtColonelViewReportClass(window)


def ltcolonels():
    master = Toplevel()
    master.title("Lieutenant Colonel Home")
    master.state("zoomed")

    img = ImageTk.PhotoImage(file='AFG.jpg')
    w, h = img.width(), img.height()
    canvas = Canvas(master, width=w, height=h, bg='blue', highlightthickness=0)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(0, 0, image=img, anchor=NW)


    menubar = Menu(master)
    file = Menu(menubar, tearoff=0)

    file.add_command(label="View Profile", command=ltcolonelview)
    file.add_command(label="Change password", command=ltcolonelpasschange)

    file.add_separator()

    file.add_command(label="Logout", command=master.destroy)

    menubar.add_cascade(label="Personal", menu=file)

    edit = Menu(menubar, tearoff=0)

    edit.add_command(label="Report Information", command=ltcolonelreportsend)
    edit.add_command(label="View Information Report", command=ltcolonelreportview)
    edit.add_command(label="View PEID Graph", command=peidgraph)

    menubar.add_cascade(label="Activities", menu=edit)
    help = Menu(menubar, tearoff=0)
    help.add_command(label="About",command=about)

    menubar.add_cascade(label="Help", menu=help)

    master.config(menu=menubar)
    master.mainloop()


#---------------------------------------------------------------------
def about():
    window = Toplevel()
    app = ViewAboutClass(window)


def majorpasschange():
    print("clicked")
    window = Toplevel()
    app = MajorGeneralChangePasswordClass(window)


def majorprofileview():
    print("clicked")
    window = Toplevel()
    app = MajorGeneralProfileViewClass(window)


def majorsecretinfosend():
    print("clicked")
    window = Toplevel()
    app = MajorSecretInformationSendClass(window)


def majorsecretinfoview():
    print("clicked")
    window = Toplevel()
    app = MajorGeneralViewReportClass(window)

def majorgeneral():
    # top = Tk()
    master = Toplevel()
    master.title("Major General Home")
    master.state("zoomed")

    img = ImageTk.PhotoImage(file='mag.jpg')
    w, h = img.width(), img.height()
    canvas = Canvas(master, width=w, height=h, bg='blue', highlightthickness=0)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(0, 0, image=img, anchor=NW)


    menubar = Menu(master)
    file = Menu(menubar, tearoff=0)

    file.add_command(label="View Profile", command=majorprofileview)
    file.add_command(label="Change password", command=majorpasschange)

    file.add_separator()

    file.add_command(label="Logout", command=master.destroy)

    menubar.add_cascade(label="Personal", menu=file)

    edit = Menu(menubar, tearoff=0)

    edit.add_command(label="Report Information", command=majorsecretinfosend)
    edit.add_command(label="Major General View Information", command=majorsecretinfoview)
    edit.add_command(label="View PEID Graph", command=peidgraph)

    menubar.add_cascade(label="Activities", menu=edit)
    help = Menu(menubar, tearoff=0)
    help.add_command(label="About",command=about)

    menubar.add_cascade(label="Help", menu=help)

    master.config(menu=menubar)
    master.mainloop()


#----------------------------------------------------------------------------------
def generalpasschange():
    print("clicked")
    window =Toplevel()
    app = GeneralChangePasswordClass(window)


def generalprofileview():
    print("clicked")
    window = Toplevel()
    app = GeneralProfileViewClass(window)


def generalsecretinfosend():
    print("clicked")
    window = Toplevel()
    app = GeneralSecretInformationSendClass(window)


def generalsecretinfoview():
    print("clicked")
    window = Toplevel()
    app = GeneralViewReportClass(window)


def peidgraph():
    print("graph clicked...")
    window = Toplevel()
    app = PerceptualEncClass(window)

def generalhome():
    master = Toplevel()
    master.title("General Home")
    master.state("zoomed")

    img = ImageTk.PhotoImage(file='gen.jpg')
    w, h = img.width(), img.height()
    canvas = Canvas(master, width=w, height=h, bg='blue', highlightthickness=0)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(0, 0, image=img, anchor=NW)


    menubar = Menu(master)
    file = Menu(menubar, tearoff=0)

    file.add_command(label="View Profile", command=generalprofileview)
    file.add_command(label="Change password", command=generalpasschange)

    file.add_separator()

    file.add_command(label="Logout", command=master.destroy)

    menubar.add_cascade(label="Personal", menu=file)

    edit = Menu(menubar, tearoff=0)

    edit.add_command(label="Report Information", command=generalsecretinfosend)
    edit.add_command(label="General View Information", command=generalsecretinfoview)
    edit.add_command(label="View PEID Graph", command=peidgraph)

    menubar.add_cascade(label="Activities", menu=edit)
    help = Menu(menubar, tearoff=0)
    help.add_command(label="About",command=about)

    menubar.add_cascade(label="Help", menu=help)

    master.config(menu=menubar)
    master.mainloop()


#-------------------------------------------------------------------------------------
def colonelpasschange():
    print("clicked")
    window = Toplevel()
    app = ColonelChangePasswordClass(window)


def colonelprofilelist():
    print("clicked")
    window = Toplevel()
    app = ColonelProfileViewClass(window)


def colonelreportsend():
    print("clicked")
    window = Toplevel()
    app = ColonelSecretInformationSendClass(window)


def colonelreportview():
    print("clicked")
    window = Toplevel()
    app = ColonelViewReportClass(window)

def colonelhome():
    master = Toplevel()
    master.title("Colonel Home")
    master.state("zoomed")

    img = ImageTk.PhotoImage(file='ads.jpg')
    w, h = img.width(), img.height()
    canvas = Canvas(master, width=w, height=h, bg='blue', highlightthickness=0)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(0, 0, image=img, anchor=NW)


    menubar = Menu(master)
    file = Menu(menubar, tearoff=0)

    file.add_command(label="View Profile", command=colonelprofilelist)
    file.add_command(label="Change password", command=colonelpasschange)

    file.add_separator()

    file.add_command(label="Logout", command=master.destroy)

    menubar.add_cascade(label="Personal", menu=file)

    edit = Menu(menubar, tearoff=0)

    edit.add_command(label="Report Information", command=colonelreportsend)
    edit.add_command(label="View Information Report", command=colonelreportview)
    edit.add_command(label="View PEID Graph", command=peidgraph)

    menubar.add_cascade(label="Activities", menu=edit)
    help = Menu(menubar, tearoff=0)
    help.add_command(label="About",command=about)

    menubar.add_cascade(label="Help", menu=help)

    master.config(menu=menubar)
    master.mainloop()


#------------------------------------------------------------------------------------
def showmyprofile():
        print("clicked")
        window = Toplevel()
        app = MyprofileClass(window)


def showchangepassword():
    print("clicked")
    window = Toplevel()
    app = AdminPasswordChangeClass(window)

def showaddnewuser():
    print("clicked")
    window =  Toplevel()
    app = AddNewOfficerClass(window)
def showremoveofficer():
    print("clicked")
    window = Toplevel()
    app = RemoveOfficerClass(window)
def idbased():
    print("clicked")
    window = Toplevel()
    app = AdminIDBasedSearchClass(window)
def rankbased():
    print("clicked")
    window = Toplevel()
    app = RankBasedSearchClass(window)
def listallofficers():
    print("clicked")
    window = Toplevel()
    app = ListAllOfficersClass(window)


def adminhome():
    master1 = Toplevel()
    master1.title("Admin Home")
    master1.state("zoomed")

    img = ImageTk.PhotoImage(file='new.jpg')
    w, h = img.width(), img.height()
    canvas = Canvas(master1, width=w, height=h, bg='blue', highlightthickness=0)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(0, 0, image=img, anchor=NW)


    menubar = Menu(master1)
    file = Menu(menubar, tearoff=0)
    #file.add_command(label="my profile")
    file.add_command(label="My Profile", command=showmyprofile)

    #file.add_command(label="New Officer Appointment")
    file.add_command(label="New Officer Appointment", command=showaddnewuser)

    #file.add_command(label="Remove Officer")
    file.add_command(label="Remove Officer", command=showremoveofficer)

    #file.add_command(label="Change Password")
    file.add_command(label="Change Password", command=showchangepassword)

    file.add_separator()
    file.add_command(label="Logout", command=master1.destroy)

    menubar.add_cascade(label="Activites", menu=file)
    edit = Menu(menubar, tearoff=0)
    #edit.add_command(label="IDBased")
    edit.add_command(label="IDBased", command=idbased)

    #edit.add_command(label="Rank Based")
    #edit.add_command(label="Rank Based", command=rankbased)

    edit.add_separator()

    #edit.add_command(label="Select All Officers")
    edit.add_command(label="Select All Officers", command=listallofficers)

    menubar.add_cascade(label="LogReport", menu=edit)
    help = Menu(menubar, tearoff=0)
    help.add_command(label="About")
    menubar.add_cascade(label="Help", menu=help)

    master1.config(menu=menubar)
    master1.mainloop()

def getuserid():
    return USER_ID

def chooseaction():
    global USER_ID
    u_name = uname.get()
    u_pass = upass.get()
    print("Username:", u_name)
    print("Password:", u_pass)

    USER_ID=u_name

    foo.USER_NAME_ID = u_name

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="army"
    )
    mycursor = mydb.cursor()

    #mycursor = createcursor()
    USERID=u_name
    sql = "select * from login where userid=%s and password=%s"
    adr = (u_name, u_pass)
    mycursor.execute(sql, adr)
    records = mycursor.fetchall()
    print("done")
    USER_TYPE = ""
    for row in records:
        USER_TYPE = row[2]
        print(USER_TYPE)
    #print("my user name is:", USER_TYPE)

    if USER_TYPE != "":
        top.withdraw()
        if USER_TYPE=="admin":
            print("admin here")
            adminhome()
        elif USER_TYPE=="colonel":
            print("colonel here")
            colonelhome()

        elif USER_TYPE=="general":
            print("general here")
            generalhome()
        elif USER_TYPE=="ltColonel":
            print("ltColonel")
            ltcolonels()
        elif USER_TYPE=="majorgeneral":
            print("majorgeneral here")
            majorgeneral()
    else:
        messagebox.showinfo("Alert","No Such User...")


def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)


def onclick():

    global USER_ID
    u_name = uname.get()
    u_pass = upass.get()
    print("Username:", u_name)
    print("Password:", u_pass)
    USER_ID=u_name

    foo.USER_NAME_ID = u_name

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="army"
    )
    mycursor = mydb.cursor()

    #mycursor = createcursor()
    #USERID=u_name

    sql = "select userid,password from login where userid=%s"
    adr=(u_name,)
    mycursor.execute(sql,adr)
    records = mycursor.fetchall()


    status=False
    USER_TYPE = ""
    PASS=""
    MY_USER=""
    for row in records:
        #print("ROW..",row)
        print("user......",row[0])
        print("password...",row[1])
        #USER_TYPE = row[0]
        #print(U)
        status=True
        if status==True:
            MY_USER=row[0]
            PASS=row[1]
            break
    if status==False:
        messagebox.showinfo("Alert", "no such user...")
    elif status==True:
        print("user......",MY_USER)
        print("PASSSSSSSSSSSSSSSSSS:",PASS)

        p=MY_USER[len(MY_USER)-2:]
        messagebox.showinfo("Alert","An OTP has send to ********"+p)

        OTP=randomString()
        print(OTP)
#------------------------------------------------------------------------------------------------
        CHECK_ID=uname.get()
        print("user id",CHECK_ID)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="army"
        )
        mycursor = mydb.cursor()

    # mycursor = createcursor()
    # USERID=u_name

        sql = "update login set password=%s where userid=%s"
        val = (OTP, CHECK_ID)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")

        response = sendPostRequest(URL, 'APQ29I7R7SS93Z42RGI8MTLNUB9FNYV8', '26TE4BLBWN8SS7LA', 'stage',CHECK_ID,'9061259158','YOUR ONE TIME PASSWORD: ' +OTP)
        #response = sendPostRequest(URL, 'APQ29I7R7SS93Z42RGI8MTLNUB9FNYV8', '26TE4BLBWN8SS7LA', 'stage', "7510625756",'9061259158', PASS)
    window = Toplevel()
    app = OtpPasswordClass(window)

    # print("my user name is:", USER_TYPE)

def randomString(stringLength=6):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase


    return ''.join(random.choice(letters) for i in range(stringLength))



#print ("Random String is ", randomString() )
#print ("Random String is ", randomString(10) )
#print ("Random String is ", randomString(6) )



def validate(e):
    #self.e=e

    if (e.isdigit()):
        return True
    else:
        return False

def loginfunction():
    large_font = ('Verdana', 15)
    large_font2 = ('Verdana', 15)
    lab1 = ('Verdana', 15)
    lab2 = ('Verdana', 15)
    bt_size = ('Verdana', 15)

    img = ImageTk.PhotoImage(file='cr.png')
    w, h = img.width(), img.height()
    canvas = Canvas(top, width=w, height=h, bg='white', highlightthickness=0)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(0, 0, image=img, anchor=NW)

    user_icon = ImageTk.PhotoImage(file="man_user.png")
    pass_icon = ImageTk.PhotoImage(file="pas.png")
    logo_icon = ImageTk.PhotoImage(file="logo.png")
    # logo_icon= PhotoImage(file="password.png")

    Login_Frame = Frame(top, bg="white")
    Login_Frame.place(x=460, y=180)
    logo_lbl = Label(Login_Frame, image=logo_icon).grid(row=0, column=0, pady=20)

    #USER_TYPE = StringVar()
    #uname = StringVar()
    #upass = StringVar()
    #windowWidth = top.winfo_reqwidth()
    #windowHeight = top.winfo_reqheight()
    #print("Width", windowWidth, "Height", windowHeight)

    #positionRight = int(top.winfo_screenwidth() / 2 - windowWidth / 2)
    #positionDown = int(top.winfo_screenheight() / 2 - windowHeight / 2)

    #top.geometry("+{}+{}".format(positionRight, positionDown))

    #top.geometry("375x250")

    top.title("Login")

    top.configure(bg="light gray")
    top.state("zoomed")

    email = Label(Login_Frame, text="User ID", font=lab1, bg="white", fg="black", image=user_icon, compound=LEFT).grid(row=1, column=0, padx=20, pady=10)

    password = Label(Login_Frame, text="Password", font=lab2, bg="white", fg="black", image=pass_icon,compound=LEFT).grid(row=2, column=0, padx=20, pady=10)


    cancel = Button(top, text="Cancel", font=bt_size,width=20,relief=RIDGE,bg="light gray",command=top.destroy).place(x=970, y=360)
    #logout = Button(top, text="Sign-in", font=bt_size, command = loadhomes).place(x=235, y=170)
    logout = Button(top, text="Sign-in", font=bt_size, width=20,relief=RIDGE,command=chooseaction).place(x=970, y=250)
    psswd = Button(top, text="Forgot Password?", font=bt_size, bg="light gray",width=20,relief=RIDGE, fg="black",command=onclick).place(x=970,y=470)
    val = top.register(validate)

    Entry(Login_Frame, textvariable=uname, width=15, font=large_font, validate="key", validatecommand=(val, '%S')).grid(row=1,column=1,padx=20,pady=10)
    # e2 = Entry(master,  width=15,font=large_font).place(x = 130, y = 30)
    # text = e2.get()
    e3 = Entry(Login_Frame, textvariable=upass, show="*", width=15, font=large_font2).grid(row=2,column=1,padx=20,pady=10)

    # e3 = Entry(master, width=15,font=large_font2).place(x = 130, y = 100)
    top.mainloop()

loginfunction()



