import tkinter
from tkinter import*
import sqlite3
import os
from tkinter import messagebox
interface=Tk()
interface.title("REGISTER")
interface.geometry("675x600")

first_name=StringVar()
second_name=StringVar()
gender=IntVar()
number=IntVar()
mail=StringVar()
password1=StringVar()
password2=StringVar()

def login():
    interface.destroy()
    os.system('login.py')

def submit():
    j=0
    name_1=first_name.get()
    name_2=second_name.get()
    gen=gender.get()
    try:
        phone=number.get()
    except:
        messagebox.showinfo("!!ERROR!!","PLEASE ENTER A VALID phone number")
        obj.func_1()
    email=mail.get()
    password=password1.get()
    if len(first_name.get()) == 0 or len(second_name.get()) == 0 or gender.get() == 0 or len(mail.get()) == 0 or len(password1.get()) == 0 or len(password2.get()) == 0 or password2.get()!= password1.get():
        messagebox.showinfo("!!ERROR!!", "PLEASE FILL IN THE DATA OR CHECK THE PASSWORD")
        obj.func_1()
    else:
        pass
    if ('@' not in email):
        messagebox.showinfo("!!ERROR!!", "PLEASE PROVIDE A VALID MAIL ID")
        obj.func_1()
    else:
        pass
    if(len(password)<6):
        messagebox.showinfo("!!ERROR!!","PLEASE ENSURE LENGTH OF PASSWORD(ATLEAST 6)")
        obj.func_1()
    else:
        if(gen == 1):
            gen='MALE'
        else:
            gen='FEMALE'
        try:
            conn = sqlite3.connect("database.db")
            print("DATABASE CONNECTED")
        except Error as e:
            print(e)
        #conn.execute("create table data(First_Name varchar(50),Second_Name varchar(50),Gender varchar(6),Phone_Number number(10),Mail_Address varchar(50),Password varchar(50));")
        print(type(name_1))
        print(name_1)
        conn.execute("insert into data(First_Name,Second_Name,Gender,Phone_Number,Mail_Address,Password)values(?,?,?,?,?,?)",(name_1,name_2,gen,phone,email,password))
        conn.commit()
        interface.destroy()
        os.system('login.py')
       
Label(interface,text="FIRST NAME",font='cambria').place(x=150,y=100)
Entry(interface,textvar=first_name,font='cambria',bd=2).place(x=350,y=100)
Label(interface,text="SECOND NAME",font='cambria').place(x=150,y=150)
Entry(interface,textvar=second_name,font='cambria',bd=2).place(x=350,y=150)
Radiobutton(interface, text="MALE",padx = 20, variable=gender,value=1,font='cambria').place(x=150,y=200)
Radiobutton(interface, text="FEMALE",padx = 20, variable=gender, value=2,font='cambria').place(x=350,y=200)
Label(interface,text="MOBILE NO",font='cambria').place(x=150,y=250)
Entry(interface,textvar=number,font='cambria',bd=2).place(x=350,y=250)
Label(interface,text="MAIL ID",font='cambria').place(x=150,y=300)
Entry(interface,textvar=mail,font='cambria',bd=2).place(x=350,y=300)
Label(interface,text="PASSWORD",font='cambria').place(x=150,y=350)
Entry(interface,textvar=password1,font='cambria',bd=2,show="*").place(x=350,y=350)
Label(interface,text="CONFIRM PASSWORD",font='cambria').place(x=150,y=400)
Entry(interface,textvar=password2,font='cambria',bd=2,show="*").place(x=350,y=400)
class A:
    def func_1(self):
        Button(interface,text="SUBMIT",command=submit).place(x=390,y=450)
obj=A()
obj.func_1()
Button(interface,text="LOGIN",command=login).place(x=450,y=450)
interface.mainloop()
