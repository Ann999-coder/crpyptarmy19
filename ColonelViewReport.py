from tkinter.ttk import *
from tkinter import *
import mysql.connector
import os
import foo
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from random import randint
import numpy
import sys
from helper import *

class ColonelViewReportClass:
    def __init__(self, top):
        large_font = ('Verdana', 14)
        large_font2 = ('Verdana', 14)
        lab1 = ('Verdana', 14)
        lab2 = ('Verdana', 14)
        bt_size = ('Verdana', 14)
        self.fpath=StringVar()
        self.top=top
        #top = Tk()
        windowWidth = top.winfo_reqwidth()
        windowHeight = top.winfo_reqheight()
        print("Width", windowWidth, "Height", windowHeight)
        positionRight = int(top.winfo_screenwidth() / 4 - windowWidth / 3)
        positionDown = int(top.winfo_screenheight() / 8 - windowHeight / 3)
        # Positions the window in the center of the page.
        top.geometry("+{}+{}".format(positionRight, positionDown))
        # top.geometry("+{}+{}".format(600, 250))
        top.geometry("1000x750")

        top.title("Colonel View Secret Info")

        ender = Label(top, text="Rank", font=("times new roman", 15, "bold")).place(x=10, y=20)

        sender = Label(top, text="Sender ID", font=("times new roman", 15, "bold")).place(x=10, y=70)

        self.combo1 = Combobox(top, font=lab2)
        self.combo1 = Combobox(top, font=lab2)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="army"
        )
        mycursor = mydb.cursor()

        sql = "select distinct usertype from login where userid in(select senderid from sendinfo)"
        mycursor.execute(sql)
        records = mycursor.fetchall()
        lst = []
        for row in records:
            print(row[0])
            lst.append(row[0])

        tp = tuple(lst)
        print(tp)
        self.combo1['values'] = tp
        self.combo1.place(x=140, y=30)
        self.combo1.bind("<<ComboboxSelected>>", self.select_Combo)

        list = Label(top, text="List",font=("times new roman", 15, "bold")).place(x=10, y=120)

        # cancel = Button(top, text = "Cancel",activebackground = "pink", activeforeground = "blue",font=bt_size).place(x = 120, y = 170)

        cancel = Button(top, text="Cancel", font=bt_size, command=top.destroy).place(x=780, y=680)
        display = Button(top, text="Display", font=bt_size,command=self.Load_Image).place(x=420, y=115)
        decode = Button(top, text="Decode", font=bt_size,command=self.Decode_Image).place(x=520, y=115)

        #c = Canvas(top, bg="pink", width="950", height="500").place(x=20, y=170)
        self.combo2 = Combobox(top, font=lab2)
        self.combo2['values'] = ("select",)
        self.combo2.place(x=140, y=70)
        self.combo2.bind("<<ComboboxSelected>>", self.select_list)

        self.combo2.place(x=140, y=70)

        self.combo3 = Combobox(top, font=lab2)
        self.combo3['values'] = "select"
        self.combo3.place(x=140, y=120)

        top.mainloop()

    def select_Combo(self, event):
        self.var_Selected = self.combo1.get()
        print("The user selected value now is:")
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="army"
        )
        mycursor = mydb.cursor()

        sql = "select distinct senderid from sendinfo where senderid in(select userid from login where usertype=%s)"
        adr = (self.var_Selected,)
        mycursor.execute(sql, adr)
        records = mycursor.fetchall()
        lst = []
        for row in records:
            print(row[0])
            lst.append(row[0])
        tups = tuple(lst)
        print("list....", lst)
        print("tuple...", tups)
        self.combo2['values'] = tups
        print(self.var_Selected)

    def select_list(self, event):
        Rec_Id = foo.USER_NAME_ID
        User_iD = self.combo2.get()
        entries = os.listdir(os.getcwd() + "\\" + Rec_Id + "\\" + "recieve" + "\\" + User_iD)
        lst = []
        for x in entries:

            if (x.endswith(".png")):
                print(x)
                lst.append(x)
            tups = tuple(lst)
            print("list....", lst)
            print("tuple...", tups)
            self.combo3['values'] = tups

    def Load_Image(self):
        messagebox.showinfo("alert","image loaded")

        Rec_Id = foo.USER_NAME_ID
        User_iD = self.combo2.get()
        fname = self.combo3.get()

        fpath = os.getcwd() + "\\" + Rec_Id + "\\" + "recieve" + "\\" + User_iD + "\\" + fname
        print("path is....",fpath)

        #-------------show image----------------------------------------

        filename=fpath

        #self.set(filename)

        canvas = Canvas(self.top, width="950", height="500")  # .place(x=20, y=210)

        img = PhotoImage(file=filename)
        canvas.create_image(0, 0, image=img, anchor=NW)

        canvas.pack()
        canvas.place(x=20, y=170)
        result=os.getcwd() + "\\" + Rec_Id + "\\" + "recieve" + "\\" +"Result" + "\\" + User_iD
        print("destination.........",result)
        if os.path.isdir(result):
            print("exists")
        else:

            print("does not exists")
            os.makedirs(result)



        mainloop()

    def Decode_Image(self):
        messagebox.showinfo("alert", "image loaded")

        Rec_Id = foo.USER_NAME_ID
        User_iD = self.combo2.get()
        fname = self.combo3.get()

        encrypt_path = os.getcwd() + "\\" + Rec_Id + "\\" + "recieve" + "\\" + User_iD + "\\" + fname
        print("path is....", encrypt_path)
        output_img = os.getcwd() + "\\" + Rec_Id + "\\" + "recieve" + "\\" + "result" + "\\" + User_iD + "\\" +fname
        print("path is....", output_img)

        #----------------------decrypt---------------

        im = Image.open(encrypt_path)
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

        #--------------------------------------------------------------------------------
        f_name = fname[:len(fname) - 4]
        Keys_Path = os.getcwd() + "\\" + Rec_Id + "\\" + "recieve" + "\\" + User_iD + "\\" + f_name + ".txt"
        print("keys path...........", Keys_Path)

        fileptr = open(Keys_Path, "r");

        # running a for loop
        lis = []
        stp = ""
        for i in fileptr:
            # print(i)  # i contains each line of the file
            stp = stp + i
            i = i.strip()
            if i.isnumeric():
                lis.append(int(i))
        # print(lis)

        string1 = stp[stp.index("Vector Kr :") + 11:stp.index("Vector Kc :")]

        sts = string1.split("\n")

        Kr = []
        for x in sts:
            x = x.strip()
            if x.isnumeric():
                Kr.append(int(x))

        print(Kr)
        print(len(Kr))  # 268

        string2 = stp[stp.index("Vector Kc :") + 11:stp.index("ITER_MAX :")]
        # print("String 2:", string2)

        stk = string2.split("\n")

        Kc = []
        for y in stk:
            y = y.strip()
            # print("Hai",y)
            if y.isnumeric():
                Kc.append(int(y))

        print(Kc)
        print(len(Kc))  # 188
        #-----------------------------------------

        #Kr=[83, 134, 183, 229, 152, 102, 210, 218, 191, 30, 177, 6, 55, 113, 206, 232, 203, 7, 197, 205, 110, 153, 3, 63, 47, 66, 28, 124, 59, 164, 61, 40, 39, 44, 38, 216, 5, 189, 6, 190, 213, 195, 210, 168, 198, 132, 59, 132, 176, 136, 67, 2, 143, 69, 150, 49, 106, 68, 189, 190, 151, 133, 184, 70, 167, 148, 159, 164, 1, 141, 219, 174, 193, 116, 228, 12, 11, 242, 224, 139, 70, 204, 224, 181, 61, 143, 187, 185, 42, 69, 212, 80, 185, 50, 183, 201, 237, 101, 87, 1, 239, 171, 92, 68, 95, 209, 11, 183, 222, 184, 238, 45, 202, 210, 127, 181, 25, 204, 137, 65, 40, 154, 154, 172, 85, 126, 247, 100, 158, 31, 61, 56, 210, 227, 178, 148, 55, 213, 158, 151, 110, 173, 184, 190, 126, 219, 210, 125, 41, 118, 98, 39, 148, 78, 89, 34, 14, 32, 83, 104, 162, 91, 158, 61, 51, 228, 217, 44, 57, 216, 9, 81, 222, 41, 127, 107, 30, 51, 64, 141, 14, 10, 241, 97, 232, 139, 249, 84, 229, 49, 134, 189, 23, 241, 250, 190, 77, 9, 108, 97, 246, 103, 34, 124, 160, 194, 118, 203, 103, 18, 86, 48, 183, 201, 149, 233, 84, 131, 211, 146, 160, 90, 93, 9, 144, 158, 186, 143, 226, 134, 8, 11, 25, 96, 175, 56, 170, 21, 152, 192, 196, 34, 115, 153, 136, 137, 29, 5, 44, 137, 80, 83, 82, 23, 94, 40, 14, 249, 4, 36, 189, 197, 234, 136, 182, 78, 32, 173]
        print("Kr Length...:",len(Kr))
        #Kc=[224, 136, 98, 15, 112, 43, 189, 7, 226, 37, 208, 42, 88, 248, 106, 73, 243, 37, 166, 31, 61, 203, 247, 109, 90, 217, 165, 34, 28, 212, 8, 74, 26, 191, 106, 211, 172, 145, 7, 163, 28, 239, 30, 176, 100, 165, 194, 42, 223, 181, 210, 22, 133, 60, 61, 141, 67, 72, 140, 147, 23, 144, 108, 8, 254, 102, 44, 144, 176, 87, 38, 150, 112, 182, 155, 38, 234, 45, 133, 189, 212, 99, 134, 129, 207, 87, 127, 43, 41, 221, 181, 215, 171, 157, 213, 47, 27, 15, 137, 132, 216, 204, 165, 22, 188, 232, 185, 217, 45, 239, 0, 124, 114, 172, 24, 108, 17, 24, 22, 105, 105, 59, 141, 26, 95, 163, 168, 239, 120, 43, 189, 194, 185, 198, 98, 87, 212, 202, 23, 18, 3, 159, 246, 134, 179, 200, 213, 104, 163, 172, 193, 6, 145, 201, 173, 233, 158, 246, 74, 135, 212, 170, 104, 4, 30, 60, 230, 250, 191, 23, 250, 228, 13, 211, 59, 180, 222, 114, 226, 169, 1, 44, 128, 93, 148, 126, 95, 173]
        print("Kc Length:",len(Kc))

        ITER_MAX=1

        """Kr = []
        Kc = []

        print('Enter value of Kr')
        print("I am here... in Kr")

        for i in range(m):
            Kr.append(int(input()))
        print("KR..........:",Kr)

        print('Enter value of Kc')
        for i in range(n):
            Kc.append(int(input()))


        print("KC..........:",Kc)

        print('Enter value of ITER_MAX')
        ITER_MAX = int(input())"""


        for iterations in range(ITER_MAX):
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
                    downshift(r, i, Kc[i])
                else:
                    upshift(r, i, Kc[i])
                if (gModulus == 0):
                    downshift(g, i, Kc[i])
                else:
                    upshift(g, i, Kc[i])
                if (bModulus == 0):
                    downshift(b, i, Kc[i])
                else:
                    upshift(b, i, Kc[i])

            # For each row
            for i in range(m):
                rTotalSum = sum(r[i])
                gTotalSum = sum(g[i])
                bTotalSum = sum(b[i])
                rModulus = rTotalSum % 2
                gModulus = gTotalSum % 2
                bModulus = bTotalSum % 2
                if (rModulus == 0):
                    r[i] = numpy.roll(r[i], -Kr[i])
                else:
                    r[i] = numpy.roll(r[i], Kr[i])
                if (gModulus == 0):
                    g[i] = numpy.roll(g[i], -Kr[i])
                else:
                    g[i] = numpy.roll(g[i], Kr[i])
                if (bModulus == 0):
                    b[i] = numpy.roll(b[i], -Kr[i])
                else:
                    b[i] = numpy.roll(b[i], Kr[i])

        for i in range(m):
            for j in range(n):
                pix[i, j] = (r[i][j], g[i][j], b[i][j])

        im.save(output_img)

        #-------------------------------------------






        out_img = os.getcwd() + "\\" + Rec_Id + "\\" + "recieve" + "\\" + "result" + "\\" + User_iD +"\\" + fname
        print("path is....", out_img)

            # -------------show image----------------------------------------

        filename = out_img

            # self.set(filename)

        canvas = Canvas(self.top, width="950", height="500")  # .place(x=20, y=210)

        img = PhotoImage(file=filename)
        canvas.create_image(0, 0, image=img, anchor=NW)

        canvas.pack()
        canvas.place(x=20, y=170)
        mainloop()

        #----------------------------------------------------------------------------------------------------------------------------
