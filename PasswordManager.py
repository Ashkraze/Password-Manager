import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
from tkinter import messagebox

window=Tk()
window.geometry("500x400")
window.resizable('false','false')
window.configure(bg="aliceblue")

def decrypt(data):
    first = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890!@#$%"
    second= "@Qqw!WE#er$R%tTYyU4uiIOo2pPaA3SsDxd1Xf6FGgHh5jJKk7LlZz8cCvV9bB0nNMm"
    xrs = data.maketrans(second,first)
    y = data.translate(xrs)
    inputtxt3.insert(1.0,y)
    
def encrypt(text):
    first = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890!@#$%"
    second= "@Qqw!WE#er$R%tTYyU4uiIOo2pPaA3SsDxd1Xf6FGgHh5jJKk7LlZz8cCvV9bB0nNMm"
    xrp = text.maketrans(first,second)
    x = text.translate(xrp)
    ascii_values = x
    return ascii_values

def clear():
    inputtxt1.delete(1.0,'end')
    inputtxt2.delete(1.0,'end')
    inputtxt3.delete(1.0,'end')

    
def savepass():
    web=inputtxt1.get(1.0,"end-1c")
    email=inputtxt2.get(1.0,"end-1c")
    pasw=inputtxt3.get(1.0,"end-1c")
    pas=(encrypt(pasw))
    print(pas)
    resr=[]
    with open("Passwordfiler.txt","r") as file:
        res=file.readlines()
        file.close
    for i in res:
        i=i.split("\n")
        resr.append(i[0])
    i=0    
    stat=0
    leng=len(res)
    while(i<leng):
        if(web==resr[i] and email==resr[i+1]):
            a_file=open("Passwordfiler.txt","r")
            listofline=a_file.readlines()
            listofline[i+2]=str(pas)+"\n"
            a_file=open("Passwordfiler.txt","w")
            a_file.writelines(listofline)
            a_file.close()
            stat=1
            messagebox.showinfo("Alert","New Password Updated")    
            break
        i+=3
    if(stat==0):
        with open("Passwordfiler.txt","a") as file:
            file.write(f"{web}\n{email}\n{pas}\n")
            file.close 
            messagebox.showinfo("Success","New Password Saved")    
    inputtxt1.delete(1.0,'end')
    inputtxt2.delete(1.0,'end')
    inputtxt3.delete(1.0,'end')


    

def openpass():
    web=inputtxt1.get(1.0,"end-1c")
    email=inputtxt2.get(1.0,"end-1c")
    resr=[]
    with open("Passwordfiler.txt","r") as file:
        res=file.readlines()
        file.close
    for i in res:            
        i=i.split("\n")
        resr.append(i[0])
    i=0    
    stat=0
    leng=len(res)
    while(i<leng):
        if(web==resr[i] and email==resr[i+1]):
            inputtxt3.delete(1.0,'end')       
            data =resr[i+2]
            #print("Key value for password is :",data)
            decrypt(data)                         
            stat=1
            break
        i+=3
    if(stat==0):
        inputtxt3.delete(1.0,'end')
        inputtxt3.insert(1.0,'No record')





b_savepass=Button(window,text="Save Password",height=2,width=20,bg="green",fg="white",font = ("slant",9),command=savepass)
b_savepass.place(relx=0.5,rely=0.65,anchor=CENTER)



b_openpass=Button(window,text="Open Saved Password",height=2,width=20,bg="blue",fg = "white",font = ("slant",9),command=openpass)
b_openpass.place(relx=0.5,rely=0.8,anchor=CENTER)



b_clear=Button(window,text="Clear All",height=2,width=10,bg="firebrick",fg="white",command=clear,font = ("slant",10))
b_clear.place(relx=0.95,rely=0.4,anchor=E)



'''l1=Label(window,text="Developed By - \nAkash Chandel",font=("arial",10,"bold"))
l1.config(fg= "black",)
l1.place(relx=0.9,rely=0.95,anchor=CENTER)
'''

l2=Label(window,text="Password Manager",font=("Arial",20,"bold"))
l2.config(bg = "aliceblue")
l2.place(relx=0.5,rely=0.1,anchor=CENTER)



inputtxt1 = tk.Text(window,height=1,width=20)
inputtxt1.place(relx=0.7,rely=0.3,anchor=E)


lbl1=tk.Label(window,text="Platform >",bg = "aliceblue",font=("Times",12,"bold"))
lbl1.place(relx=0.1,rely=0.3,anchor=W)



inputtxt2 = tk.Text(window,height=1,width=20)
inputtxt2.place(relx=0.7,rely=0.4,anchor=E)


lbl2=tk.Label(window,text="E-Mail Id >",fg = "Black",font=("Times",12,"bold"),bg = "aliceblue")
lbl2.place(relx=0.1,rely=0.4,anchor=W)



inputtxt3 = tk.Text(window,height=1,width=20)
inputtxt3.place(relx=0.7,rely=0.5,anchor=E)

lbl3=tk.Label(window,text="Password > ",font=("Times",12,"bold"),bg = "aliceblue")
lbl3.place(relx=0.1,rely=0.5,anchor=W)


window.mainloop()
