import tkinter
from tkinter import*
import sqlite3
import os
from tkinter import messagebox

interface=Tk()
interface.title("ADMIN")
interface.geometry("300x300")
username=StringVar()
password=StringVar()

def back():
    interface.destroy()
    os.system('login.py')
def submit():
    j=0
    try:
        conn=sqlite3.connect('admin_data.db')
        print("CONNECTED")
    except:
        print("NOT CONNECTED")
    m=conn.execute("select Username,Password from data")
    user=username.get()
    key=password.get()
    if(len(user)==0 or len(key)==0):
        messagebox.showinfo("!!ERROR!!", "PLEASE FILL IN THE DATA")
        obj.func_1()
    else:
        pass
    if(len(key)<6):
        messagebox.showinfo("!!ERROR!!","WRONG PASSWORD")
        obj.func_1()
    else:
        pass
    for i in m:
        if(user==i[0]):
            if(key==i[1]):
                conn.commit()
                interface.destroy()
                os.system('routes.py')
            else:
                messagebox.showinfo("!!ERROR!!","PASSWORD IS INCORRECT")
        else:
            messagebox.showinfo("!!ERROR!!","USERNAME NOT PRESENT")
Label(interface,text="USERNAME: ",font='cambria').place(x=15,y=100)
Entry(interface,textvar=username,font='cambria',bd=2).place(x=105,y=100)
Label(interface,text="PASSWORD: ",font='cambria').place(x=15,y=150)
Entry(interface,textvar=password,font='cambria',bd=2,show="*").place(x=105,y=150)
class A:
    def func_1(self):
        Button(interface,text="SUBMIT",command=submit).place(x=130,y=210)

Button(interface,text="<--BACK",command=back).place(x=200,y=210)
        
        
obj=A()
obj.func_1()
interface.mainloop()

