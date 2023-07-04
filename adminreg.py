from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import sqlite3 as sql
import re
class AdminReg:
 def __init__(self,root):
    self.c_name=StringVar()
    self.name=re.compile("[a-z]+")
    self.c_pwd=StringVar()
    self.pwd=re.compile("[a-z]+")
    
    self.c_repwd=StringVar()
    self.repwd=re.compile("[a-z]+")
    self.c_gmail=StringVar()
    self.id_no=StringVar()
    
    self.con=sql.connect(database='facemaskadminreg.sqlite')
    self.cursor=self.con.cursor()
    self.cursor.execute("create table if not exists registration(name varchar(20),username varchar(20) primary key,gmailid varchar(50),password varchar(30))")

    self.root=root 
    self.root.geometry('1280x700+0+0')
    self.root.title("FaceMask Detecation Admin Registration")
    self.root.resizable(False,False)
    self.backgroundImage=ImageTk.PhotoImage(file='images/Aiback.jpg')
    self.bgLabel=Label(self.root,image=self.backgroundImage)
    self.bgLabel.place(x=0,y=0)
        #frame
    self.signupFrame=Frame(self.root,bg ='cornflowerblue')
    self.signupFrame.place(x=80,y=100)
    # Load Image
    self.logoImage=ImageTk.PhotoImage(file='images/face-mask.png')
    self.logoLabel=Label(self.signupFrame,image=self.logoImage)
    self.logoLabel.grid(row=0,column=0,columnspan=2,pady=10) 

    #name
    self.nameImage=ImageTk.PhotoImage(file='images/id-card.png')
    self.namelabel=Label(self.signupFrame,image=self.nameImage,text='Name',
    compound=LEFT,font=('times new roman',20,'bold'),bg='cornflowerblue')
    self.namelabel.grid(row=1,column=0,padx=20,pady=10,sticky='w')
    self.nameEntry=Entry(self.signupFrame,font=('times new roman',20),bd=5,fg='royalblue',textvariable=self.c_name)
    self.nameEntry.grid(row=1,column=1,padx=20,pady=10)
    
    self.usernameImage=ImageTk.PhotoImage(file='images/ai.png')
    self.usernamelabel=Label(self.signupFrame,image=self.usernameImage,text='Username',
    compound=LEFT,font=('times new roman',20,'bold'),bg='cornflowerblue')
    self.usernamelabel.grid(row=2,column=0,padx=20,pady=10,sticky='w')
    
    
    self.usernameEntry=Entry(self.signupFrame,font=('times new roman',20),bd=5,fg='royalblue')
    self.usernameEntry.grid(row=2,column=1,padx=20,pady=10)
    #gmail 
    self.gmailImage=ImageTk.PhotoImage(file='images/gmail.png')
    self.gmaillabel=Label(self.signupFrame,image=self.gmailImage,text='Gmail Id',
    compound=LEFT,font=('times new roman',20,'bold'),bg='cornflowerblue')
    self.gmaillabel.grid(row=3,column=0,padx=20,pady=10,sticky='w')


    self.gmailEntry=Entry(self.signupFrame,font=('times new roman',20),bd=5,fg='royalblue')
    self.gmailEntry.grid(row=3,column=1,padx=20,pady=10)
    #password
    self.passwordImage=PhotoImage(file='images/secure.png')
    self.passwordlabel=Label(self.signupFrame,image=self.passwordImage,text='Password',
    compound=LEFT,font=('times new roman',20,'bold'),bg='cornflowerblue')
    self.passwordlabel.grid(row=4,column=0,padx=20,pady=10,sticky='w') 

    self.passwordEntry=Entry(self.signupFrame,font=('times new roman',20),bd=5,fg='royalblue',show="*",textvariable=self.c_pwd)
    self.passwordEntry.grid(row=4,column=1,padx=20,pady=10)

    self.repasswordlabel=Label(self.signupFrame,text='Re-Password',
    font=('times new roman',20,'bold'),bg='cornflowerblue')
    self.repasswordlabel.grid(row=5,column=0,padx=20,pady=10,sticky='w')

    self.repasswordEntry=Entry(self.signupFrame,font=('times new roman',20),bd=5,fg='royalblue',show="*",textvariable=self.c_repwd)
    self.repasswordEntry.grid(row=5,column=1,padx=20,pady=10)

    self.signupButton=Button(self.signupFrame,text="Register",command=self.insert,font=('time new roman',14,'bold'),
    width=15,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2')
    self.signupButton.grid(row=6,column=0,pady=10)

    self.loginButton=Button(self.signupFrame,text="Sign In",font=('time new roman',14,'bold'),
    width=15,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2',command=self.signin)
    self.loginButton.grid(row=6,column=1,pady=10)

    self.clearButton=Button(self.signupFrame,text="Clear",font=('time new roman',14,'bold'),
    width=15,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2',command=self.clearEntry)
    self.clearButton.grid(row=7,column=0,pady=10)

    self.exitButton=Button(self.signupFrame,text="Exit",font=('time new roman',14,'bold'),
    width=15,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2',command=self.exit)
    self.exitButton.grid(row=7,column=1,pady=10)
    try:
        con=sql.connect(database='facemaskadminreg.sqlite')
    except:
        print("Connection is not created")
 def clearEntry(self):
            self.nameEntry.delete(first=0,last=100)
            self.usernameEntry.delete(first=0,last=100)
            self.gmailEntry.delete(first=0,last=100)
            self.passwordEntry.delete(first=0,last=100)
            self.repasswordEntry.delete(first=0,last=100)
 #exit
 def exit(self):
        op=messagebox.askyesno("Exit","Do you want to really Exit")
        if(op>0):
            self.root.destroy()            
        else:
            return

 def error(self):
            messagebox.showerror("Error","password  not same")    
 def insert(self):
    name=self.nameEntry.get()
    user=self.usernameEntry.get()
    gmail=self.gmailEntry.get()
    email="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
   
    password=self.passwordEntry.get()
    repassword=self.repasswordEntry.get()
    #insert="insert into registration values('%s','%s','%s','%s')"%(name,user,gmail,password);
    # values=(nameEntry.get(),usernameEntry.get(),gmailEntry.get(),passwordEntry.get())
    if(name=='' or user==''or gmail=='' or password=='' or repassword==''):
        messagebox.showwarning('Warning',"Field Can't be empty")
    elif(password !=repassword):
        messagebox.showwarning('Warning'," password EntryField Can't be matched")
    else: 
        #gmail verification  
        if(re.search(email,gmail)):
            insertData="insert into registration(name,username,gmailid,password) values(?,?,?,?)"
            values=(name,user,gmail,password)
            c=self.cursor.execute(insertData,values)
            self.con.commit()        
            self.clearEntry()
            messagebox.showinfo("Database Created","your data inserted")
        else:
            messagebox.showwarning('Warning',"Wrong Email Id")

       

 def signin(self):
    self.root.destroy()
    import login

  

root=Tk()
obj=AdminReg(root)
root.mainloop()