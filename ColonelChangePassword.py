#!/usr/bin/env python

from tkinter import *

import foo
from AdminHome import *
from tkinter import messagebox


class ColonelChangePasswordClass:
    def __init__(self, master):
        large_font = ('Verdana', 15)
        large_font2 = ('Verdana', 15)
        lab1 = ('Verdana', 15)
        lab2 = ('Verdana', 15)
        bt_size = ('Verdana', 15)
        self.master = master

        self.cname = StringVar()
        self.npass = StringVar()
        self.rpass = StringVar()

        windowWidth = master.winfo_reqwidth()
        windowHeight = master.winfo_reqheight()
        print("Width", windowWidth, "Height", windowHeight)

        positionRight = int(master.winfo_screenwidth() / 3 - windowWidth / 2)
        positionDown = int(master.winfo_screenheight() / 3 - windowHeight / 2)

        master.geometry("+{}+{}".format(positionRight, positionDown))

        master.geometry("450x300")

        master.title("Admin Password Change")
        master.configure(bg="light gray")

        self.email = Label(master, text="Current Password", font=lab1,bg="light gray").place(x=30, y=30)

        self.password = Label(master, text="New Password", font=lab2,bg="light gray").place(x=30, y=100)

        self.rpassword = Label(master, text="ReType Password", font=lab2,bg="light gray").place(x=30, y=170)

        self.cancel = Button(master, text="Cancel", font=bt_size, command=master.destroy).place(x=133, y=230)
        #logout = Button(master, text="Sign-up", font=bt_size).place(x=133, y=200)

        self.login = Button(master, text="Apply", font=bt_size, command=self.commands).place(x=250, y=230)

        e3= Entry(master, textvariable=self.cname, width=15, font=large_font, show="*").place(x=220, y=30)
        e3 = Entry(master, textvariable=self.npass, show="*", width=15, font=large_font2).place(x=220, y=100)
        e4 = Entry(master, textvariable=self.rpass, show="*", width=15, font=large_font2).place(x=220, y=170)

        # e3 = Entry(master, width=15,font=large_font2).place(x = 130, y = 100)

    def commands(self):
        print('Button is pressed!')


        self.c_pass = self.cname.get()
        self.n_pass = self.npass.get()
        self.r_pass = self.rpass.get()

        print("Current password:", self.c_pass)
        print("new Password:", self.n_pass)
        print("Re type Password:", self.r_pass)

        P_WORD=foo.USER_NAME_ID
        if len(self.n_pass) >= 4 and len(self.n_pass) <= 10:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="root",
                database="army"
            )
            mycursor = mydb.cursor()

            if self.n_pass == self.r_pass:

                sql = "UPDATE login SET password = %s WHERE userid = %s and password=%s"
                val = (self.n_pass, P_WORD, self.c_pass)

                mycursor.execute(sql, val)
                cnt = mycursor.rowcount
                print("CNT.....:", cnt)

                mydb.commit()

                if cnt == 1:
                    messagebox.showinfo("Alert", "Successfully updated...")
                    self.master.destroy()
                    self.master.update()
                else:
                    messagebox.showinfo("Alert", "Incorrect password...")

            else:
                messagebox.showinfo("Alert", "Password mismatching...")
        else:
            messagebox.showinfo("Alert", "Password must contain min 4 and max 10...")

#root = Tk()

#cls = AdminPasswordChangeClass(root)

#root.mainloop()
