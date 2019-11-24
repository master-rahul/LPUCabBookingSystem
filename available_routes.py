import tkinter
from tkinter import*
import sqlite3
import os
from tkinter import messagebox

interface=Tk()
interface.title("AVAILABLE ROUTES")
interface.geometry("1000x600")
conn=sqlite3.connect("routes.db")
m=conn.execute("select Location,Destination,Fare,Time,Distance from data")    
j=1
def exit():
    interface.destroy()
def login():
    interface.destroy()
    os.system('login.py')
Label(interface,text="                     LOCATION                        DESTINATION                                        COST                    TIME              DISTANCE",font='cambria',bd=2).pack(side='top')
Label (interface, text="").pack()
for i in m:
    a=["LOCATION :    ",i[0],"DESTINATION :    ",i[1],"COST :    ",i[2],"TIME :    ",i[3],"DISTANCE :",i[4]]
    Label(interface,text=a,font='cambria',bd=2).pack()
conn.commit()
Button(interface,text="EXIT",command=exit).pack(side='bottom', padx = 5, pady = 5);
Button(interface,text="<--BACK",command=login).pack(side='bottom', padx = 5, pady = 5)

interface.mainloop()
