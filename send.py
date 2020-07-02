from tkinter.ttk import *
from tkinter import *
#import ttk

class app():

    def _init_(self):
        self.root = Tk()
        self.fill_Combo()
        self.root.mainloop()

    def fill_Combo(self):
        self.combo1= Combobox(self.root,height=1, width=20)
        self.combo1['values'] = ("Kerala","Tamilnadu","Andra","Maharashtra")
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
        lst=[]
        lst.append(self.var_Selected)
        tup=tuple(lst)
        self.combo2['values']=tup
        print (self.var_Selected)
        # Any other function you want to use as function(self.var_Selected) or a function that gets self

app()