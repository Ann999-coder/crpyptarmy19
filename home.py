from tkinter import Toplevel, Button, Tk, Menu


class SampleHome():
    def __init__(self, master):
        master.title("MyHome")
        menubar = Menu(master)
        file = Menu(menubar, tearoff=0)
        file.add_command(label="New")
        file.add_command(label="Open")
        file.add_command(label="Save")
        file.add_command(label="Save as...")
        file.add_command(label="Close")

        file.add_separator()

        file.add_command(label="Exit", command=master.destroy)

        menubar.add_cascade(label="File", menu=file)
        edit = Menu(menubar, tearoff=2)
        edit.add_command(label="Undo")

        edit.add_separator()

        edit.add_command(label="Cut")
        edit.add_command(label="Copy")
        edit.add_command(label="Paste")
        edit.add_command(label="Delete")
        edit.add_command(label="Select All")

        menubar.add_cascade(label="Edit", menu=edit)
        help = Menu(menubar, tearoff=0)
        help.add_command(label="About")
        menubar.add_cascade(label="Help", menu=help)

        master.config(menu=menubar)
        master.state('zoomed')
    # def close_window2(self):
    # self.master.destroy()

# root = Tk()

# root.title("Login")

# root.geometry("375x250")

# cls = SampleHome(root)

# root.mainloop()
# top.mainloop()
