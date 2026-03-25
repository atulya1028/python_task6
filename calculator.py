# step1: importing
from tkinter import *

#step2: gui interaction
window = Tk()
window.geometry('500x500')

# step3: adding inputs

# ENTRY BOX
e = Entry(window, width= 35,borderwidth=5)
e.place(x = 20, y = 20)

#BUTTONS
def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0,str(result + str(num)))

b = Button(window, text = '1',width=12,command=lambda: click(1))
b.place(x = 10, y=80)

b = Button(window, text = '2',width=12, command=lambda: click(2))
b.place(x = 120, y=80)

b = Button(window, text = '3',width=12, command=lambda: click(3))
b.place(x = 230, y=80)

b = Button(window, text = '4',width=12, command=lambda: click(4))
b.place(x = 10, y=130)

b = Button(window, text = '5',width=12, command=lambda: click(5))
b.place(x = 120, y=130)

b = Button(window, text = '6',width=12, command=lambda: click(6))
b.place(x = 230, y=130)

b = Button(window, text = '7',width=12, command=lambda: click(7))
b.place(x = 10, y=180)

b = Button(window, text = '8',width=12, command=lambda: click(8))
b.place(x = 120, y=180)

b = Button(window, text = '9',width=12, command=lambda: click(9))
b.place(x = 230, y=180)

b = Button(window, text = '0',width=12, command=lambda: click(0))
b.place(x = 10, y=230)

#OPERATORS
def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text = '+',width=12,command= add)
b.place(x = 120, y=230)

def sub():
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text = '-',width=12,command=sub)
b.place(x = 230, y=230)

def mult():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text = '*',width=12,command=mult)
b.place(x = 10, y=280)

def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text = '/',width=12,command=div)
b.place(x = 120, y=280)

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0,i + int(n2))
    elif math == "subtraction":
        e.insert(0,i - int(n2))
    elif math == "multiplication":
        e.insert(0,i * int(n2))
    elif math == "division":
        e.insert(0,i / int(n2))

b = Button(window, text = '=',width=12,command=equal)
b.place(x = 230, y=280)

def clear():
    e.delete(0, END)

b = Button(window, text = 'clear',width=12,command= clear)
b.place(x = 10, y=340)


# step4: mainloop
mainloop()