#Import the required library
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from tkinter import ttk
#Create an instance of tkinter window
win= Tk()
win.title("BUDGET MANAGER")

def graph():
    plt.title("budget Management")
    plt.ylabel("Expense")
    plt.xlabel("xaxis")
    plt.legend()
    hist=np.random.normal(2000,5000,6000)
    plt.hist(hist)
    plt.show()
def myfunc():
    print("RETRY")
def getvals():
    print("budget manager")
    global sum
    n1=totalvalue.get()
    n2=ex1value.get()
    n3=ex2value.get()
    n4=ex3value.get()
    n5=ex4value.get()
    n6=ex5value.get()
    n7=ex6value.get()
    n8=ex7value.get()
    sum=n2+n3+n4+n5+n6+n7+n8
    res.config(text=sum)
    print(f"{totalvalue.get(), ex1value.get(), ex2value.get(), ex3value.get(), ex4value.get(),ex5value.get(),ex6value.get(),ex7value.get()} ")

    with open("recordss.txt", "a") as f:
        f.write(f"{totalvalue.get(), ex1value.get(), ex2value.get(), ex3value.get(), ex4value.get(),ex5value.get(),ex6value.get(),ex7value.get(),}\n ")

#Make image resize dynamically
def resizer(e):
    global bg1, resized_bg, new_bg
    bg1=Image.open("money.jpg")
    resized_bg=bg1.resize((e.width, e.height),Image.ANTIALIAS)
    new_bg=ImageTk.PhotoImage(resized_bg)
    canvas.create_image(0, 0, image=new_bg, anchor="nw")


#Define the geometry of the window
win.geometry("610x430")
#Load the image

mainmenu = Menu(win)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
win.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
win.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="QUIT", command=quit)
win.config(menu=mainmenu)
mainmenu.add_cascade(label="QUIT", menu=m3)
bg= ImageTk.PhotoImage(Image.open("money.jpg"))
#Create a canvas
canvas = Canvas(win,width= 200, height= 200)
canvas.pack(expand=True, fill= BOTH)
#Add the image in the canvas
canvas.create_image(0,0,image=bg, anchor="nw")
#Add a text in canvas

Label(canvas, fg="red", text="Budget manager", justify='center', font="comicsansms 35 bold", pady=10).grid(row=0, column=3)
total = tkinter.Label(canvas, text="Total Amount")
ex1 = tkinter.Label(canvas, text="expense 1")
ex2 = tkinter.Label(canvas, text="expense 2")
ex3 = tkinter.Label(canvas, text="expense 3")
ex4 = tkinter.Label(canvas, text="expense 4")
ex5 = tkinter.Label(canvas, text="expense 5")
ex6 = tkinter.Label(canvas, text="expense 6")
ex7 = tkinter.Label(canvas, text="expense 7")
res = tkinter.Label(canvas,font=20)


#Pack text for our form
total.grid(row=2, column=2)
ex1.grid(row=3, column=2)
ex2.grid(row=4, column=2)
ex3.grid(row=5, column=2)
ex4.grid(row=6, column=2)
ex5.grid(row=7, column=2)
ex6.grid(row=8, column=2)
ex7.grid(row=9, column=2)

# Tkinter variable for storing entries
totalvalue = IntVar()
ex1value = IntVar()
ex2value = IntVar()
ex3value = IntVar()
ex4value = IntVar()
ex5value = IntVar()
ex6value = IntVar()
ex7value = IntVar()


#Entries for our form
totalentry = Entry(canvas, textvariable=totalvalue)
ex1entry = Entry(canvas, textvariable=ex1value)
ex2entry = Entry(canvas, textvariable=ex2value)
ex3entry = Entry(canvas, textvariable=ex3value)
ex4entry = Entry(canvas, textvariable=ex4value)
ex5entry = Entry(canvas, textvariable=ex5value)
ex6entry = Entry(canvas, textvariable=ex6value)
ex7entry = Entry(canvas, textvariable=ex7value)

# Packing the Entries
totalentry.grid(row=2, column=3)
ex1entry.grid(row=3, column=3)
ex2entry.grid(row=4, column=3)
ex3entry.grid(row=5, column=3)
ex4entry.grid(row=6, column=3)
ex5entry.grid(row=7, column=3)
ex6entry.grid(row=8,column=3)
ex7entry.grid(row=9,column=3)


#Button & packing it and assigning it a command
Button(canvas, text="total", command=getvals).grid(row=10, column=3)
mybutton=Button(win,text="Graph",command=graph)
mybutton.pack()
win.bind('<Configure>', resizer)
win.mainloop()