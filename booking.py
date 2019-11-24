import tkinter
from tkinter import*
import sqlite3
import os
from tkinter import messagebox
from tkcalendar import Calendar

import random
interface=Tk()
interface.title("BOOKING")
interface.geometry("630x700")

cal = Calendar(interface, local="fr_FR.UTF-8",font="Arial 12",cursor="hand1", year=2018, month=10, day=30)
des_data=StringVar()
time=StringVar()
date=StringVar()
new=StringVar()
new1=StringVar()
new2=StringVar()
location=StringVar(interface)
destination=StringVar(interface)
hour=StringVar(interface)
minute=StringVar(interface)
conn=sqlite3.connect("routes.db")
c=conn.execute("select distinct Location from data")
loc=list(c.fetchall())
location.set(loc[0])
conn1=sqlite3.connect('Dest.db')
def exit1():
    interface.destroy()
def nex():
    new1=location.get()
    new2=destination.get()
    one=0
    two=0
    for h1 in new1:
        one=one+1
    new3=new1[2:one-3]
    for h2 in new2:
        two=two+1
    new4=new2[2:two-3]
    print(new3)
    print(new4)
    if(new3==new4):
        messagebox.showinfo("!!ERROR!!", "PLEASE FILL IN THE DATA")
        obj.func_1()
    data=conn.execute('select Fare,Time,Distance from data where Location=? and Destination=?',(new3,new4))
    for i in data:
        a=i[0]
        b=i[1]
        c=i[2]
    conn.commit()
        
    def submit():
        
        date=cal.selection_get()
        hou=hour.get()
        minu=minute.get()
        conn2=sqlite3.connect('transaction.db')
        abc=random.randint(0,9999999999999999)
        print(abc)
        #conn2.execute('create table data(Session_Id varcahr(20)primary key,Location varchar(50),Destination varchar(50),Fare varchar(50),Time varchar(50),Distance varchar(50),Date varchar(50),Hour varchar(50),Minute varchar(50));')
        try:
            conn2.execute('insert into data(Session_Id,Location,Destination,Fare,Time,Distance,Date,Hour,Minute) values(?,?,?,?,?,?,?,?,?)',(abc,new3,new4,a,b,c,date,hou,minu))
        except:
            print('sorry')
        conn2.commit()
        f=open("session_id.txt","a")
        f.write("\n"+ str(abc))
        f.close()
        interface1=Tk()
        interface1.title("SESSION")
        interface1.geometry("230x100")
        conn4=sqlite3.connect('transaction.db')
        def done():
            interface.destroy()
            interface1.destroy()
            
        
        Label(interface1,text="Please Note Down:",font='cambria',bd=2).place(x=10,y=10)
        Label(interface1,text="SESSION_ID",font='cambria',bd=2).place(x=10,y=50)
        Label(interface1,text=abc,font='cambria',bd=2).place(x=10,y=70)
        Button(interface1, text="DONE", command=done).place(x=180,y=70)
        conn4.commit()
        interface1.mainloop()
        
        
        
    def last():
        Button(interface, text="SUBMIT", command=submit).place(x=350,y=550)        
    def print_sel():
        hour.set("00")
        minute.set("00")
        Label(interface,text="TIMING:",font='cambria',bd=2).place(x=100,y=510)
        OptionMenu(interface,hour,"00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24").place(x=325,y=510)
        OptionMenu(interface,minute,"00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59").place(x=380,y=510)
        Button(interface, text="OK", command=last).place(x=450,y=512)
    Label(interface,text="FARE :",font='cambria',bd=2).place(x=100,y=120)
    Label(interface,text=a,font='cambria',bd=2).place(x=350,y=120)
    Label(interface,text="Rupees",font='cambria',bd=2).place(x=400,y=120)
    Label(interface,text="TIME :",font='cambria',bd=2).place(x=100,y=170)
    Label(interface,text=b,font='cambria',bd=2).place(x=350,y=170)
    Label(interface,text="Minutes",font='cambria',bd=2).place(x=400,y=170)
    Label(interface,text="DISTANCE :",font='cambria',bd=2).place(x=100,y=220)
    Label(interface,text=c,font='cambria',bd=2).place(x=350,y=220)
    Label(interface,text="Meters",font='cambria',bd=2).place(x=400,y=220)
    Label(interface,text="DATE :",font='cambria',bd=2).place(x=100,y=350)
    cal.place(x=200,y=270)
    Button(interface, text="OK", command=print_sel).place(x=550,y=360)
    
def ok():
    des_data=location.get()
    co=0
    for hee in des_data:
        co=co+1
    new=des_data[2:co-3]
    conn1.execute('''insert into data(destinate)values(?)''',(new,))
    he=conn1.execute('select destinate from data')
    count=0
    for loop in he:
        count=count+1
    hell(des_data,count)
def hell(des_data,count):
    
    y=conn1.execute("select destinate from data")
    des1=list(y.fetchall())
    des_data=des1[count-1]
    z=conn.execute("select distinct Destination from data where Location=?",(des_data))
    #c.execute(n)
    des=list(z.fetchall())
    destination.set(des[0])
    OptionMenu(interface,destination,*des).place(x=350,y=70)
    Label(interface,text="SECLECT DESTINATION :",font='cambria',bd=2).place(x=100,y=70)
    obj.func_1()
    

    

Label(interface,text="SECLECT LOCATION :",font='cambria',bd=2).place(x=100,y=20)
OptionMenu(interface,location,*loc).place(x=350,y=20)
Button(interface, text="OK", command=ok).place(x=500,y=20)
class A:
    def func_1(self):
        Button(interface, text="OK", command=nex).place(x=500,y=70)
obj=A()

        
Button(interface,text="EXIT",command=exit1).place(x=300,y=650);
conn.commit()
conn1.commit()
interface.mainloop()
