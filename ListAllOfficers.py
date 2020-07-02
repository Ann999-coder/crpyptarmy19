from tkinter import *
import mysql.connector

#ListAllOfficersClass
import mysql.connector


class ListAllOfficersClass:
    def __init__(self, top):

        #top = Tk()

        lab2 = ('Verdana', 14)
        bt_size = ('Verdana', 14)

        windowWidth = top.winfo_reqwidth()
        windowHeight = top.winfo_reqheight()
        print("Width", windowWidth, "Height", windowHeight)

        positionRight = int(top.winfo_screenwidth() / 3 - windowWidth / 2)
        positionDown = int(top.winfo_screenheight() / 3 - windowHeight / 2)

        # Positions the window in the center of the page.
        top.geometry("+{}+{}".format(positionRight, positionDown))
        # top.geometry("+{}+{}".format(600, 250))
        top.geometry("900x650")

        top.title("List All Officers")

        listbox = Listbox(top, width=200, height=20)

        str = 'xyz\t12345\tabc'

        # no argument is passed
        # default tabsize is 8
        result = str.expandtabs(15)

        data= "User ID"+"\tUser Name\tGender\tDate of birth\tDesignation\t\tQualification\t\tAddress\t\tCity\t\tPIN"
        result=data.expandtabs(15)

        listbox.insert(1, result)

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="army"
        )
        mycursor = mydb.cursor()
        sql= "select * from adduser"
        mycursor.execute(sql)
        records = mycursor.fetchall()
        i=2
        for row in records:
            data2=row[0]+"\t"+row[1] +"\t"+ row[2]+"\t"+row[3]+"\t"+row[4] +"\t"+ row[5]+"\t"+row[6]+"\t"+row[7] +"\t"+ row[8]
            result2=data2.expandtabs(23)
            listbox.insert(i, result2)
            #print(row[0])


        listbox.place(x=10, y=50)
        cancel = Button(top, text="Cancel", font=bt_size, command=top.destroy).place(x=350, y=380)

        top.mainloop()

#top= Tk()
#cp= ListAllDoctorsClass(top)

