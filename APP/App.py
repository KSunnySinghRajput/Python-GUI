try:
    # python 3.x
    from tkinter import *
    from tkinter.ttk import *
    import tkinter as tk
    from tkinter import messagebox as tmsg, colorchooser, commondialog, filedialog, font, messagebox, scrolledtext, simpledialog, dnd

    # from tkinter import Tk , BOTH, Botton
    # from tkinter.ttk import Frame, Label, Style

except ImportError:
    # python 2.x
    from Tkinter import *
    import Tkinter as tk

from PIL import Image, ImageTk


def help():
    print("How Can I Help You?")
    tmsg.showinfo("Help", "We will Help You")
    # You can Also Show The Return Value of .showinfo Class
    # r = tmsg.showinfo("Help", "We will Help You")
    # print(r)

def feedback():
    print("Please Give Us Feedback")
    tmsg.askyesno("Rate Us", "Please Give Us Feedback")
    # You can Also Show The Return Value of .askyesno Class
    # r = tmsg.askyesno("Feedback", "Please Give Us Feedback")
    # print(r)

def rate():
    print("Please Rate Us")
    r = tmsg.askquestion("Rate Us", "Are You Satisfied With Our Service")
    # You can Also Show The Return Value of .askquestion Class
    # r = tmsg.askquestion("Rate Us", "Are You Satisfied With Our Service")
    # print(r)
    if r == "yes":
        msg = "Thank You, Plesae write some valuable comment about us"
    else:
        msg = "Please Give Us Some Suggestions to Improve"
    tmsg.showinfo("User Experience",msg)


def getmoney():
    print(f"The money you will get {slider_v.get()}")
    tmsg.showinfo("Value", f"You have applied for {slider_v.get()}k money")
    

class App(Tk):
    def __init__(self):
        super().__init__()
        try:
            print("App Version : 0.0.0.1")
            print("TK Version  : ", tk.TkVersion)
            print("TCL Version : ", tk.TclVersion)
        except:
            print("App Error Occure")
            exit()
        self.App()
        self.mainloop()

    def App(self):
        self.UIinit()
        self.MenusOrSubmenus()
        self.InputAndPack()

    def UIinit(self):
        self.title("Menu and SubMenu")

        # GEOMETRY("WIDTHxHEIGHT")
        self.geometry("850x500")

        # MINSIZE(WIDTH,HEIGHT)
        self.minsize(200, 100)

        # MAXSIZE(WIDTH,HEIGHT)
        self.maxsize(self.winfo_screenwidth(),self.winfo_screenheight())

        photo = ImageTk.PhotoImage(file="res/icon.png")
        self.iconphoto(False, photo)

        # self.eval('tk::PlaceWindow . center')
        # self.overrideredirect(1)
        # self.attributes("-alpha", 0.3)
        # self.resizable(False, False)  # This code helps to disable windows from resizing
        # self.state('zoomed')
        self['background'] = '#58F'
        self.configure(background='White')



    def MenusOrSubmenus(self):
        menu_bar = Menu(self)
        sub_menu1 = Menu(menu_bar, tearoff=0)
        sub_menu1.add_command(label="New")
        sub_menu1.add_command(label="Open")
        sub_menu1.add_command(label="Save")
        sub_menu1.add_command(label="Save As")
        sub_menu1.add_separator()
        sub_menu1.add_command(label="Page Setup")
        sub_menu1.add_command(label="Print")
        sub_menu1.add_separator()
        sub_menu1.add_command(label="Exit")

        sub_menu2 = Menu(menu_bar, tearoff=0)
        sub_menu2.add_command(label="Undo")
        sub_menu2.add_separator()
        sub_menu2.add_command(label="Cut")
        sub_menu2.add_command(label="Copy")
        sub_menu2.add_command(label="Paste")
        sub_menu2.add_command(label="Delete")
        sub_menu2.add_separator()
        sub_menu2.add_command(label="Find")
        sub_menu2.add_command(label="Find Next")
        sub_menu2.add_command(label="Replace")
        sub_menu2.add_command(label="Go To")
        sub_menu2.add_separator()
        sub_menu2.add_command(label="Select All")
        sub_menu2.add_command(label="Date/Time")

        menu_bar.add_cascade(label="File", menu=sub_menu1)
        menu_bar.add_cascade(label="Edit", menu=sub_menu2)

        self.config(menu=menu_bar)

    def InputAndPack(self):
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)

        # label
        label = Label(text="This Is My First GUI")
        label.pack()

        # img Lable
        img = ImageTk.PhotoImage(Image.open("res/nature1.jpg"))
        image_label = Label(image=img)
        image_label.pack()

        # Radiobutton
        radio = IntVar()
        lbl = Label(text="Favourite programming language:")
        lbl.pack()

        R1 = Radiobutton(self, text="C", variable=radio, value=1, command=selection)
        R2 = Radiobutton(self, text="C++", variable=radio,  value=2, command=selection)
        R3 = Radiobutton(self, text="Java", variable=radio,  value=3, command=selection)

        R1.pack(anchor=W)
        R2.pack(anchor=W)
        R3.pack(anchor=W)

        # text
        label_content = Label(text='''Python is an interpreted, object-oriented, high-level programming language with dynamic \nsemantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very \nattractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing \ncomponents together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of \nprogram maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The \nPython interpreter and the extensive standard library are available in source or binary form without charge for all \nmajor platforms, and can be freely distributed.''', bg="red", fg="white", font=("arial", 10, "bold"), padx=30, pady=30, borderwidth=5, relief=SUNKEN)
        label_content.pack(anchor="ne")


            def form(self,parrent=None):
        
        def live(self, *args): 
            value = self.var.get() 
            text = "{}".format(value) if value else "" 
            self.label.config(text=text) 
        
        def print_contents(event):
            print("Hi. The current entry content is:",self.contents.get())
    
        def say_hi(self):
            print("hi there, everyone!")
            
        if not parent:
            parent = self
            
        self.var = StringVar() 
        self.var.trace("w", self.show_message) 
        self.entry = Entry(self, textvariable=self.var) 
        self.btn = Button(self, text="Clear", command=lambda: self.var.set("")) 
        self.label = Label(self) 
        self.entry.pack() 
        self.btn.pack() 
        self.label.pack() 


if __name__ == "__main__":
    app = App()
