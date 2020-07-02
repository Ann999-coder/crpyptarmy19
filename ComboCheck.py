from tkinter.ttk import *
from tkinter import *
import mysql.connector
#import ttk

class app():

    def __init__(self):
        self.root = Tk()
        self.fill_Combo()
        self.root.mainloop()

    def fill_Combo(self):
        self.combo1= Combobox(self.root,height=1, width=20)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="army"
        )
        mycursor = mydb.cursor()

        sql = "select distinct designation from adduser"
        mycursor.execute(sql)
        records = mycursor.fetchall()
        lst = []
        for row in records:
            print(row[0])
            lst.append(row[0])

        tp = tuple(lst)
        print(tp)
        self.combo1['values'] = (tp)
        self.combo1.current(0)
        self.combo1.place(x=5, y = 75)
        self.combo1.bind("<<ComboboxSelected>>",self.select_Combo)
        lst=[]

        self.combo2 = Combobox(self.root, height=1, width=20)
        self.combo2['values'] = ("select", )
        self.combo2.current(0)
        self.combo2.place(x=5, y=110)

    def select_Combo(self, event):
        self.var_Selected = self.combo1.get()
        print( "The user selected value now is:")
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="army"
        )
        mycursor = mydb.cursor()

        sql = "select userid from login where usertype=%s"
        adr=(self.var_Selected,)
        mycursor.execute(sql,adr)
        records = mycursor.fetchall()
        lst = []
        for row in records:
            print(row[0])
            lst.append(row[0])
        tup = tuple(lst)
        self.combo2['values'] = (tup)
        print(self.var_Selected)

    # Any other function you want to use as function(self.var_Selected) or a function that gets self

app()
