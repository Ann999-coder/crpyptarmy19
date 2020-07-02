from tkinter import filedialog
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import foo
import mysql.connector
import os
from datetime import date
import time
from random import randint
import numpy
import sys
from helper import *




class ColonelSecretInformationSendClass:
    def __init__(self, top):
        large_font = ('Verdana', 14)
        large_font2 = ('Verdana', 14)
        lab1 = ('Verdana', 14)
        lab2 = ('Verdana', 14)
        bt_size = ('Verdana', 14)
        self.top = top

        # top = Tk()
        self.fpath = StringVar()

        windowWidth = top.winfo_reqwidth()
        windowHeight = top.winfo_reqheight()
        print("Width", windowWidth, "Height", windowHeight)

        positionRight = int(top.winfo_screenwidth() / 4 - windowWidth / 3)
        positionDown = int(top.winfo_screenheight() / 12 - windowHeight / 3)

        # Positions the window in the center of the page.
        top.geometry("+{}+{}".format(positionRight, positionDown))
        # top.geometry("+{}+{}".format(600, 250))
        top.geometry("1000x750")

        top.title("Colonel Information Passing")

        ender = Label(top, text="Rank", font=("times new roman", 15, "bold")).place(x=10, y=20)

# ---------------------------------------------------------------------------------------------------------
        self.combo1 = Combobox(top)
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
        self.combo1['values'] = tp
        self.combo1.place(x=160, y=20)
        self.combo1.bind("<<ComboboxSelected>>", self.select_Combo)
        lst = []
        # --------------------------------------------------------------------------------------------------------
        senderid = Label(top, text="Receiver ID", font=("times new roman", 15, "bold")).place(x=10, y=50)
        self.combo2 = Combobox(top)
        self.combo2['values'] = ("select",)
        self.combo2.place(x=160, y=50)

        image = Label(top, text="Image Path", font=("times new roman", 15, "bold")).place(x=10, y=80)

        report = Button(top, text="Report", font=bt_size,command=self.sendaction).place(x=900, y=680)
        cancel = Button(top, text="Cancel", font=bt_size, command=top.destroy).place(x=780, y=680)

        browse = Button(top, text="Browse", font=bt_size, command=self.browsefunc).place(x=450, y=70)


        e3 = Entry(top, width=25, font=large_font2, textvariable=self.fpath).place(x=140, y=80)

        top.mainloop()

    def select_Combo(self, event):
        self.var_Selected = self.combo1.get()
        MY_ID=foo.USER_NAME_ID
        print("The user selected value now is:")
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="army"
        )
        mycursor = mydb.cursor()

        sql = "select userid from login where usertype=%s and userid!=%s"
        adr = (self.var_Selected,MY_ID)
        mycursor.execute(sql, adr)
        records = mycursor.fetchall()
        lst = []
        for row in records:
            #print(row[0])
            lst.append(row[0])
        tups = tuple(lst)
        #print("list....",lst)
        #print("tuple...",tups)
        self.combo2['values'] = tups
        #print(self.var_Selected)



    def browsefunc(self):
        try:
            filename = filedialog.askopenfilename()

            self.fpath.set(filename)

            canvas = Canvas(self.top, width="950", height="500")  # .place(x=20, y=210)

            img = PhotoImage(file=filename)
            canvas.create_image(0, 0, image=img, anchor=NW)

            canvas.pack()
            canvas.place(x=20, y=150)
            mainloop()
        except:
            messagebox.showinfo("Alert", "only png images are supported...")

    def sendaction(self):
        today = date.today()
        #print("Today's date:", today)

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        #print("Current Time:", current_time)

        self.rec_id = self.combo2.get()
        #print("selected second box", self.rec_id)

        send_id = foo.USER_NAME_ID




        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="army"
        )
        mycursor = mydb.cursor()

        # mycursor = createcursor()
        """print("recieverid", self.rec_id)
        print("sender id", send_id)"""


        sql = "insert into sendinfo(senderid,recieverid,date,time)VALUES(%s,%s,%s,%s)"
        adr = (send_id, self.rec_id,today,current_time)
        mycursor.execute(sql, adr)

        mydb.commit()
#-------------------------------------------------------------------------------------------------------
        User_iD = foo.USER_NAME_ID
        Rec_Id=self.combo2.get()

        pat1 = os.getcwd() + "/"+User_iD + "/send" + "/"+Rec_Id;
        pat = os.getcwd() + "/" + User_iD + "/recieve";
        pat2=os.getcwd() + "/"+ Rec_Id + "/recieve" + "/"+User_iD;


        """print("path1",pat)
        print("path2",pat1)
        print("path3", pat2)"""

        if os.path.isdir(pat2):
            print("exists")
        else:

            print("does not exists")
            os.makedirs(pat2)

        if os.path.isdir(pat):
            print("exists")
        else:

            print("does not exists")
            os.makedirs(pat)

        if os.path.isdir(pat1):
            print("exists")
        else:

            print("does not exists")
            os.makedirs(pat1)


        #print(mycursor.rowcount, "record inserted.")
        self.current_path=self.fpath.get()

        #print("current path",self.current_path)
        my_path = self.current_path
        fname=my_path[my_path.rindex("/"):]
        #send_path=os.getcwd()+"\\"+User_iD+"\\"+"send"+"\\"+Rec_Id+ fname
        #rec_path = os.getcwd() + "\\" + Rec_Id + "\\" + "recieve" + "\\" + User_iD + fname
        #print("send path is.......................",send_path)
        #print("rec path is.......................", rec_path)

        #---------------------listing path-----------------------------------------------------------------------------------------

        #---------------------------------------------------------------




        #----------------------encrypt----------------------------------------
        im = Image.open(self.current_path)
        pix = im.load()

        # Obtaining the RGB matrices
        r = []
        g = []
        b = []
        for i in range(im.size[0]):
            r.append([])
            g.append([])
            b.append([])
            for j in range(im.size[1]):
                rgbPerPixel = pix[i, j]
                r[i].append(rgbPerPixel[0])
                g[i].append(rgbPerPixel[1])
                b[i].append(rgbPerPixel[2])

        m = im.size[0]
        n = im.size[1]

        # Vectors Kr and Kc
        alpha = 8
        Kr = [randint(0, pow(2, alpha) - 1) for i in range(m)]
        Kc = [randint(0, pow(2, alpha) - 1) for i in range(n)]
        ITER_MAX = 1

        #print('Vector Kr : ', Kr)
        #print('Vector Kc : ', Kc)

        f = open('keys.txt', 'w+')
        f.write('Vector Kr : \n')
        #-------------------------------------------------------------------
        entries = os.listdir(os.getcwd() + "\\" + Rec_Id + "\\" + "recieve" + "\\" + User_iD)

        check=os.getcwd() + "\\" + Rec_Id + "\\" + "recieve" + "\\" + User_iD

        print("Entries....:",check)
        file_count = 0
        for fn in entries:
            file_count = file_count + 1
            print("File name.................:",fn)
        print("file count:", file_count)
        f_name = str(file_count)

        #print("File Name......:",f_name)

        if file_count == 0:
            f_name = str(1)
        else:
            pk = (file_count // 2) + 1
            f_name = str(pk)
        rec_path = os.getcwd() + "\\" + Rec_Id + "\\" + "recieve" + "\\" + User_iD + "\\" + str(f_name) + ".png"

        send_path=os.getcwd() + "\\" + User_iD + "\\" + "send" + "\\" + Rec_Id + "\\" + str(f_name) + ".png"
        text_file = os.getcwd() + "\\" + Rec_Id + "\\" + "recieve" + "\\" + User_iD + "\\" + str(f_name) + ".txt"
        f4 = open(text_file, "w+")


        #--------------------------------------------------------------------

        f4.write('Vector Kr : \n')


        print("the kr path is.......",f4)
        for a in Kr:
            f.write(str(a) + '\n')
            f4.write(str(a) + '\n')
        f4.write('Vector Kc : \n')
        f.write('Vector Kc : \n')
        for a in Kc:
            f.write(str(a) + '\n')
            f4.write(str(a) + '\n')
        f4.write('ITER_MAX : \n')
        f4.write(str(ITER_MAX) + '\n')
        f.write('ITER_MAX : \n')
        f.write(str(ITER_MAX) + '\n')

        for iterations in range(ITER_MAX):
            # For each row
            for i in range(m):
                rTotalSum = sum(r[i])
                gTotalSum = sum(g[i])
                bTotalSum = sum(b[i])
                rModulus = rTotalSum % 2
                gModulus = gTotalSum % 2
                bModulus = bTotalSum % 2
                if (rModulus == 0):
                    r[i] = numpy.roll(r[i], Kr[i])
                else:
                    r[i] = numpy.roll(r[i], -Kr[i])
                if (gModulus == 0):
                    g[i] = numpy.roll(g[i], Kr[i])
                else:
                    g[i] = numpy.roll(g[i], -Kr[i])
                if (bModulus == 0):
                    b[i] = numpy.roll(b[i], Kr[i])
                else:
                    b[i] = numpy.roll(b[i], -Kr[i])
            # For each column
            for i in range(n):
                rTotalSum = 0
                gTotalSum = 0
                bTotalSum = 0
                for j in range(m):
                    rTotalSum += r[j][i]
                    gTotalSum += g[j][i]
                    bTotalSum += b[j][i]
                rModulus = rTotalSum % 2
                gModulus = gTotalSum % 2
                bModulus = bTotalSum % 2
                if (rModulus == 0):
                    upshift(r, i, Kc[i])
                else:
                    downshift(r, i, Kc[i])
                if (gModulus == 0):
                    upshift(g, i, Kc[i])
                else:
                    downshift(g, i, Kc[i])
                if (bModulus == 0):
                    upshift(b, i, Kc[i])
                else:
                    downshift(b, i, Kc[i])
            # For each row
            for i in range(m):
                for j in range(n):
                    if (i % 2 == 1):
                        r[i][j] = r[i][j] ^ Kc[j]
                        g[i][j] = g[i][j] ^ Kc[j]
                        b[i][j] = b[i][j] ^ Kc[j]
                    else:
                        r[i][j] = r[i][j] ^ rotate180(Kc[j])
                        g[i][j] = g[i][j] ^ rotate180(Kc[j])
                        b[i][j] = b[i][j] ^ rotate180(Kc[j])
            # For each column
            for j in range(n):
                for i in range(m):
                    if (j % 2 == 0):
                        r[i][j] = r[i][j] ^ Kr[i]
                        g[i][j] = g[i][j] ^ Kr[i]
                        b[i][j] = b[i][j] ^ Kr[i]
                    else:
                        r[i][j] = r[i][j] ^ rotate180(Kr[i])
                        g[i][j] = g[i][j] ^ rotate180(Kr[i])
                        b[i][j] = b[i][j] ^ rotate180(Kr[i])

        for i in range(m):
            for j in range(n):
                pix[i, j] = (r[i][j], g[i][j], b[i][j])

        #im.save('encrypted_images/' + 'pic1.png')



        im.save(send_path)
        im.save(rec_path)
        messagebox.showinfo("Alert", "Message has been send...")

        #im.save(pat1)


        #----------------------------------------------


#root = Tk()

#cp = ColonelSecretInformationSendClass(root)
#root.mainloop()
