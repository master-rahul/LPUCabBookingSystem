import tkinter
from tkinter import*
import sqlite3
import os
from tkinter import messagebox
interface=Tk()
interface.title("ADMIN CREATION")
interface.geometry("675x600")

username=StringVar()
password=StringVar()
def submit():
   
    user=username.get()
    pass1=password.get()
    if len(password.get()) == 0 or len(username.get())==0:
        messagebox.showinfo("!!ERROR!!", "PLEASE FILL IN THE DATA")
        obj.func_1()
    else:
        pass
    if(len(pass1)<6):
        messagebox.showinfo("!!ERROR!!","PLEASE ENSURE LENGTH OF PASSWORD(ATLEAST 6)")
        obj.func_1()
    else:
        try:
            conn = sqlite3.connect("admin_data.db")
            print("DATABASE CONNECTED")
        except Error as e:
            print(e)
        #conn.execute("create table data(Username varchar(50),Password varchar(50));")
        conn.execute("insert into data(Username,Password)values(?,?)",(user,pass1))
        conn.commit()
        interface.destroy()



Label(interface,text="USERNAME",font='cambria').place(x=150,y=100)
Entry(interface,textvar=username,font='cambria',bd=2).place(x=350,y=100)
Label(interface,text="PASSWORD",font='cambria').place(x=150,y=150)
Entry(interface,textvar=password,font='cambria',bd=2,show="*").place(x=350,y=150)
class A:
    def func_1(self):
        Button(interface,text="SUBMIT",command=submit).place(x=400,y=200)
obj=A()
obj.func_1()
interface.mainloop()
