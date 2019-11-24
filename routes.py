import tkinter
from tkinter import*
import sqlite3
import os
from tkinter import messagebox

interface=Tk()
interface.title("ROUTES")
interface.geometry("600x600")
location=StringVar()
destination=StringVar()
cost=IntVar()
time=IntVar()
distance=IntVar()


def submit():
    j=0
    try:
        conn=sqlite3.connect('routes.db')
        print("CONNECTED")
    except:
        print("NOT CONNECTED")
    m=conn.execute("select Location,Destination from data")    
    loc=location.get()
    des=destination.get()
      
    
    try:
        cost_1=cost.get()
        time_1=time.get()
        path=distance.get()
    except:
        messagebox.showinfo("!!ERROR!!", "PLEASE ENTER CORRECT COST")
        obj.func_1()
    if(len(loc)==0 or len(des)==0 or cost_1 ==0 or time==0 or distance==0):
        messagebox.showinfo("!!ERROR!!", "PLEASE FILL IN THE DATA")
        obj.func_1()
    else:
        for i in m:
            if(loc==i[0] and des ==i[1]):
                messagebox.showinfo("!!ERROR!!", "PLEASE FILL NEW DATA")
                obj.func_1()
            else:
                pass
        # conn.execute("create table data(Location varchar(50),Destination varchar(50), Fare number(10), Time number(10),Distance number(10));")
        conn.execute("insert into data(Location,Destination,Fare,Time,Distance) values(?,?,?,?,?)",(loc,des,cost_1,time_1,path))
        conn.execute("insert into data(Location,Destination,Fare,Time,Distance) values(?,?,?,?,?)",(des,loc,cost_1,time_1,path))
        conn.commit()
        interface.destroy()
        os.system('available_routes.py')
Label(interface,text="LOCATION: ",font='cambria').place(x=15,y=100)
Entry(interface,textvar=location,font='cambria',bd=2).place(x=105,y=100)
Label(interface,text="DESTINATION: ",font='cambria').place(x=15,y=150)
Entry(interface,textvar=destination,font='cambria',bd=2).place(x=105,y=150)
Label(interface,text="COST: ",font='cambria').place(x=15,y=200)
Entry(interface,textvar=cost,font='cambria',bd=2).place(x=105,y=200)
Label(interface,text="TIME: ",font='cambria').place(x=15,y=250)
Entry(interface,textvar=time,font='cambria',bd=2).place(x=105,y=250)
Label(interface,text="DISTANCE: ",font='cambria').place(x=15,y=300)
Entry(interface,textvar=distance,font='cambria',bd=2).place(x=105,y=300)

class A:
    def func_1(self):
        Button(interface,text="SUBMIT",command=submit).place(x=200,y=350)        
obj=A()
obj.func_1()
interface.mainloop()
