from tkinter import *
from tkinter import messagebox
from ZAKI74 import *
var = Tk()
var.title('pgcd and ppcm')
var.geometry('300x200')
v1 = StringVar()
v2 = StringVar()
l1 = Label(var, text = 'Enter first number :').place(x= 10, y=20)
e1= Entry(var,textvariable=v1).place(x=120,y=20)
l2 = Label(var, text = 'Enter second number :').place(x= 10, y=50)
e2= Entry(var, textvariable=v2).place(x=129.5,y=50)
c1 = IntVar()
c2 = IntVar()
pg = Checkbutton(var, text='PGCD',variable=c1, onvalue=1,offvalue= 0).place(x=10,y=80)
pc = Checkbutton(var, text='PPCM',variable=c1, onvalue=2,offvalue= 0).place(x=10,y=100)
def buton():
    chek1 = c1.get()
    num1 = eval(v1.get())
    num2 = eval(v2.get())
    if chek1 == 1:
        c = pgcd(num1,num2)
        a = Label(var,text= "Resultat = " + str(c)).place(x=80,y=140)
    elif chek1 == 2:
        c = ppcm(num1,num2)
        a = Label(var,text= "Resultat = " + str(c)).place(x=80,y=140)
        
    else :
        messagebox.showerror("Error", "Sorry, you did not Choose PGCD or PPCM")
        
b = Button(var, text='calculation', command=buton).place(x=120,y=100)
var.mainloop()
