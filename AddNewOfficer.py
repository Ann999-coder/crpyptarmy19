import mysql.connector
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
class AddNewOfficerClass:
    def __init__(self,top):
        self.top=top
        large_font = ('Verdana', 15)
        large_font2 = ('Verdana', 15)
        large_font3 = ('Verdana', 15)
        lab1 = ('Verdana', 11)
        lab2 = ('Verdana', 15)
        lab3 = ('Verdana', 12)

        large_font = ('Verdana', 15)
        large_font2 = ('Verdana', 15)
        large_font3 = ('Verdana', 15)
        lab1 = ('Verdana', 11)
        lab2 = ('Verdana', 15)

        bt_size = ('Verdana', 15)

        #top = Tk()

        # top.state("zoomed")

        self.uid = StringVar()
        self.upass=StringVar()
        self.cpass=StringVar()
        self.uname = StringVar()
        self.dob = StringVar()
        self.qualification = StringVar()
        self.gender = StringVar()
        self.designation = StringVar()
        self.address = StringVar()
        self.city = StringVar()
        self.pin = StringVar()
        windowWidth = top.winfo_reqwidth()
        windowHeight = top.winfo_reqheight()
        print("Width", windowWidth, "Height", windowHeight)

        positionRight = int(top.winfo_screenwidth() / 3 - windowWidth / 3)
        positionDown = int(top.winfo_screenheight() / 5 - windowHeight / 3)

        # Positions the window in the center of the page.
        top.geometry("+{}+{}".format(positionRight, positionDown))
        # top.geometry("+{}+{}".format(600, 250))

        top.geometry("800x800")

        top.title("ADD NEW OFFICER")

        top.configure(bg="light gray")

        userid = Label(top, text="User Id",font=("times new roman", 15, "bold"), bg="light gray").place(x=10, y=30)
        password = Label(top, text="password", font=("times new roman", 15, "bold"),bg="light gray").place(x=10, y=80)
        confirmpassword=Label(top, text="confirm password", font=("times new roman", 15, "bold"),bg="light gray").place(x=10, y=130)
        name = Label(top, text="Name", font=("times new roman", 15, "bold"),bg="light gray").place(x=10, y=180)
        dob =Label(top, text="DOB(yyyy-mm-dd)", font=("times new roman", 15, "bold"),bg="light gray").place(x=10, y=230)
        gender = Label(top, text="Gender", font=("times new roman", 15, "bold"),bg="light gray").place(x=10, y=280)
        rad1 = Radiobutton(top, text='male',value='male',variable=self.gender, font=lab1, )
        rad1.place(x=250, y=280)
        rad2 = Radiobutton(top, text='female',value='female',variable=self.gender, font=lab1)
        rad2.place(x=350, y=280)
        qualification =Label(top, text="Qualification", font=("times new roman", 15, "bold"),bg="light gray").place(x=10, y=330)
        designation = Label(top, text="Designation", font=("times new roman", 15, "bold"),bg="light gray").place(x=10, y=380)

        combo = Combobox(top,textvariabl=self.designation,font=lab1)
        combo['values'] = ("general", "colonel", "ltColonel", "majorgeneral", "Text")
        combo.current(3)
        combo.place(x=250, y=380)

        address = Label(top, text="Address", font=("times new roman", 15, "bold"),bg="light gray").place(x=10, y=430)
        city = Label(top, text="City", font=("times new roman", 15, "bold"),bg="light gray").place(x=10, y=480)
        pin = Label(top, text="Pin", font=("times new roman", 15, "bold"),bg="light gray").place(x=10, y=530)

        login = Button(top, text="ADD", font=bt_size, command=self.adduser).place(x=250, y=580)
        # cancel = Button(top, text = "Cancel",activebackground = "pink", activeforeground = "blue",font=bt_size).place(x = 120, y = 170)
        cancel = Button(top, text="Cancel", font=bt_size, command=top.destroy).place(x=350, y=580)

        val = top.register(self.validate)

        e1 = Entry(top,textvariable=self.uid, width=15, font=large_font, validate="key", validatecommand=(val, '%S')).place(x=250, y=30)
        e2 = Entry(top,textvariable=self.upass,show="*", width=15, font=large_font2).place(x=250, y=80)
        e22= Entry(top,textvariable=self.cpass,show="*", width=15, font=large_font2).place(x=250, y=130)
        val4 = top.register(self.validatename)
        e3 = Entry(top, textvariable=self.uname,width=15, font=large_font2, validate="key", validatecommand=(val4, '%S')).place(x=250, y=180)

        val2 = top.register(self.validate_date)
        e4 = Entry(top,textvariable=self.dob, width=15, font=large_font2, validate="key", validatecommand=(val2, '%S')).place(x=250, y=230)
        date=Button(top,text="DOB",font=lab3,command=self.example).place(x=455,y=230)
        e5 = Entry(top, textvariable=self.qualification,width=15, font=large_font2).place(x=250, y=330)
        e5 = Entry(top,textvariable=self.address, width=15, font=large_font2).place(x=250, y=430)
        e6 = Entry(top,textvariable=self.city, width=15,font=large_font2).place(x=250, y=480)
        val3 = top.register(self.validate_date)
        e7= Entry(top,textvariable=self.pin, width=15, font=large_font2, validate="key", validatecommand=(val3, '%S')).place(x=250, y=530)
        top.mainloop()

    def adduser(self):


        print('Button is pressed!')

        # self.e2.get()
        self.u_id = self.uid.get()
        self.u_pass=self.upass.get()
        self.c_pass = self.cpass.get()
        self.u_name = self.uname.get()
        self.u_dob = self.dob.get()
        self.u_qualification = self.qualification.get()
        self.u_gender = self.gender.get()
        self.u_designation = self.designation.get()
        self.u_address = self.address.get()
        self.u_city = self.city.get()
        self.u_pin = self.pin.get()
        print("Userid:", self.u_id)
        print("psswd:", self.u_pass)
        print("username:", self.u_name)
        print("dob:", self.u_dob)
        print("qualification:", self.u_qualification)
        print("gender:", self.u_gender)
        print("designation:", self.u_designation)
        print("address:", self.u_address)
        print("city:", self.u_city)
        print("pin:", self.u_pin)

        if (self.u_address!="" and self.u_designation!="" and self.u_dob!="" and self.u_gender!="" and self.u_name!="" and self.u_pass!=""):
            if (len(self.u_pin)== 6 and len(self.u_id)==10):
                if len(self.u_pass) >= 4 and len(self.u_pass) <= 10:
                    if self.u_pass == self.c_pass:

                        try:

                            mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="army"
                            )
                            mycursor = mydb.cursor()

                            sql = "insert into adduser(userid,name,dob,qualification,gender,designation,address,city,pin)value(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            adr = (self.u_id,self.u_name, self.u_dob,self.u_qualification,self.u_gender,self.u_designation,self.u_address,self.u_city,self.u_pin)
                            cp=mycursor.execute(sql,adr)
                            print(cp)

                            sql2 = "insert into login(userid,password,usertype)value(%s,%s,%s)"
                            adr2 = (self.u_id,self.u_pass , self.u_designation)

                            mycursor2 = mydb.cursor()
                            mycursor2.execute(sql2, adr2)


                            mydb.commit()
                            if mycursor:
                                messagebox.showinfo("Alert", "Successfully inserted...")

                                print("successfully inserted")
                            # self.top.destroy()
                            # self.top.withdraw()
                            self.top.destroy()
                            self.top.update()
                        except:
                            messagebox.showinfo("Alert", "insertion failed...")
                    else:
                        messagebox.showinfo("Alert","password mismatching")

                else:
                    messagebox.showinfo("Alert", "password must contain minimum 4 characters and maximum 10 characters...")

            else:
                    messagebox.showinfo("Alert","INVALID...")
        else:
            list_alert=[]
            if len(self.u_id)==0:
                list_alert.append("user id missing")
            if len(self.u_name)==0:
                list_alert.append("name missing")
            if len(self.u_pass)==0:
                list_alert.append("password missing")
            if len(self.u_gender)==0:
                list_alert.append("gender missing")
            if len(self.u_dob)==0:
                list_alert.append("Date of birth missing")
            if len(self.u_designation)==0:
                list_alert.append("designation missing")
            if len(self.u_qualification)==0:
                list_alert.append("qualification missing")
            if len(self.u_address)==0:
                list_alert.append("address missing")
            if len(self.u_city)==0:
                list_alert.append("city missing")
            if len(self.u_pin)==0:
                list_alert.append("pin missing")









            alert=""
            for x in list_alert:
                alert=alert+x
            print("Alert.....",alert)
            messagebox.showinfo("alert",alert)

    def validate(self, e):
        self.e=e

        if (self.e.isdigit()):
            return True
        else:
            return False
    def validatename(self, e):
        self.e=e

        if (self.e.isalpha()):
            return True

        elif self.e== ' ':
            return True
        else:
            return False

    def example(self):
        tps=Toplevel()
        def print_sel():
            print(cal.selection_get())
            self.dob.set(cal.selection_get())
            tps.destroy()

        cal = Calendar(tps,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=2018, month=2, day=5)
        cal.pack(fill="both", expand=True)
        Button(tps, text="ok", command=print_sel).pack()

    def validate_date(self, e):
        self.e = e

        if self.e=="-":
            return True

        elif self.e.isdigit():
            return True
        else:
            return False
    def validate_pin(self, e):
        self.e = e

        if self.e.isdigit():
            return True
        else:
            return False



    #self.uid=self.uid.strip()
    #self.u_name=sef.u_name.strip()
    #self.u_dob = self.dob.strip()
    #self.u_qualification = self.qualification.strip()
    #self.u_gender = self.gender.strip()
    #self.u_designation = self.designation.strip()
    #self.u_address = self.address.strip()
    #self.u_city = self.city.strip()
    #self.u_pin = self.pin.strip()




