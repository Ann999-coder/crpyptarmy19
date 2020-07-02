from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *

#RemoveOfficerClass
import mysql.connector

import foo


class RemoveOfficerClass:
    def __init__(self, top):
        self.top = top
        large_font = ('Verdana', 15)
        large_font2 = ('Verdana', 15)
        large_font3 = ('Verdana', 15)
        lab1 = ('Verdana', 15)
        lab2 = ('Verdana', 15)

        large_font = ('Verdana', 15)
        large_font2 = ('Verdana', 15)
        large_font3 = ('Verdana', 15)
        lab1 = ('Verdana', 15)
        lab2 = ('Verdana', 15)

        bt_size = ('Verdana', 15)

        # top = Tk()

        self.uname = StringVar()
        self.upass = StringVar()
        self.gender= StringVar()
        self.dob = StringVar()
        self.address = StringVar()
        self.city = StringVar()
        self.pin = StringVar()
        self.designation= StringVar()

        # top.state("zoomed")
        windowWidth = top.winfo_reqwidth()
        windowHeight = top.winfo_reqheight()
        print("Width", windowWidth, "Height", windowHeight)

        positionRight = int(top.winfo_screenwidth() / 3 - windowWidth / 2)
        positionDown = int(top.winfo_screenheight() / 3 - windowHeight / 2)

        # Positions the window in the center of the page.
        top.geometry("+{}+{}".format(positionRight, positionDown))
        # top.geometry("+{}+{}".format(600, 250))
        top.geometry("500x500")

        top.title("Remove profile")
        userid = Label(top, text="Enter ID", font=lab1).place(x=10, y=30)
        password = Label(top, text="Gender", font=lab2).place(x=10, y=80)
        name = Label(top, text="Name", font=lab2).place(x=10, y=130)
        gender = Label(top, text="Designation", font=lab2).place(x=10, y=180)

        """rad1 = Radiobutton(top, text='male', font=lab1, value=1)
        rad1.place(x=200, y=180)
        rad2 = Radiobutton(top, text='female', variable=self.gender,font=lab1, value=2)
        rad2.place(x=300, y=180)"""

        designation = Label(top, text="Qualification",  font=lab2).place(x=10, y=230)



        address = Label(top, text="Address", font=lab2).place(x=10, y=280)
        city = Label(top, text="City", font=lab2).place(x=10, y=330)
        pin = Label(top, text="Pin", font=lab2).place(x=10, y=380)
        login = Button(top, text="Remove", font=bt_size , command=self.removeuser).place(x=300, y=430)
        cancel = Button(top, text="Cancel", font=bt_size, command=top.destroy).place(x=200, y=430)
        e8 = Button(top, text="search", font=bt_size, command=self.searchuser).place(x=410, y=30)

        val = top.register(self.validate)

        e1 = Entry(top, width=15, textvariable=self.uname, font=large_font2,  validate="key", validatecommand=(val, '%S')).place(x=200, y=30)
        e2 = Entry(top, state=DISABLED, width=15, textvariable=self.upass, font=large_font2).place(x=200, y=80)
        e3 = Entry(top, state=DISABLED, width=15, textvariable=self.dob, font=large_font2).place(x=200, y=130)
        e9 = Entry(top, state=DISABLED, width=15, textvariable=self.designation, font=large_font2).place(x=200, y=230)

        e22 = Entry(top, state=DISABLED,width=15, textvariable=self.gender, font=large_font2).place(x=200, y=180)

        e5 = Entry(top, state=DISABLED,width=15,textvariable=self.address, font=large_font2).place(x=200, y=280)
        e6 = Entry(top,state=DISABLED, width=15,textvariable=self.city, font=large_font2).place(x=200, y=330)
        e7 = Entry(top,state=DISABLED, width=15, textvariable=self.pin,font=large_font2).place(x=200, y=380)


        top.mainloop()
    def validate(self, e):
        self.e=e

        if (self.e.isalpha()):
            return True

        if self.e == "_":
            return True
        elif self.e.isdigit():
            return True
        else:
            return False

    def searchuser(self):
        print("serching..")

        self.userdata = self.uname.get()
        print("Inputed Data......:", self.userdata)
        #self.upass.set(self.userdata)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="army"
        )
        print("Inputed Data......:", self.userdata)
        mycursor = mydb.cursor()
        sql="select * from adduser where userid=%s"
        val=(self.userdata,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        if(not myresult):
            messagebox.showinfo("Alert", "No Such User........")

        print("success...")
        for record in myresult:
            print("Data....", record)
            self.upass.set(record[2])
            self.dob.set(record[1])
            self.city.set(record[7])
            self.gender.set(record[4])
            self.designation.set(record[5])
            self.address.set(record[6])
            self.city.set(record[7])
            self.pin.set(record[8])


    def removeuser(self):
        print("clicked")
        self.userdata = self.uname.get()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="army"
        )
        print("Inputed Data......:", self.userdata)
        print("foo in remove..............:" , foo.USER_NAME_ID)
        curid=foo.USER_NAME_ID

        mycursor = mydb.cursor()

        mycursor2 = mydb.cursor()

        sql = "delete from adduser where userid = %s"
        val=(self.userdata,)
        mycursor.execute(sql,val)
        #mydb.commit()

        sql2 = "delete from login where userid = %s"
        val2 = (self.userdata,)
        mycursor2.execute(sql2, val2)

        mydb.commit()

        if mycursor and mycursor2:
            messagebox.showinfo("Alert", "Successfully Removed...")
            self.top.destroy()
            self.top.update()

        # records = mycursor.fetchall()
#top=Tk()
#cp= RemoveOfficerClass(top)
