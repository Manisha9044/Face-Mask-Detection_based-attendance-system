from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import sqlite3 as sql
import re 
class LogIn:
 def __init__(self,root):
    self.c_uname=StringVar()
    self.uname=re.compile("[a-z]+")
    self.c_pwd=StringVar()
    self.pwd=re.compile("[a-z]+")
    
    self.root=root 
    self.root.geometry('1280x700+0+0')
    self.root.title("FaceMask Detecation Management Admin Login")
    self.root.resizable(False,False)
    self.backgroundImage=ImageTk.PhotoImage(file='images/Aiback.jpg')
    self.bgLabel=Label(self.root,image=self.backgroundImage)
    self.bgLabel.place(x=0,y=0)
        #frame
    self.loginFrame=Frame(self.root,bg ='cornflowerblue')
    self.loginFrame.place(x=80,y=150)
    # Load Image
    self.logoImage=ImageTk.PhotoImage(file='images/face-mask.png')
    self.logoLabel=Label(self.loginFrame,image=self.logoImage)
    self.logoLabel.grid(row=0,column=0,columnspan=2,pady=10) 

    self.usernameImage=ImageTk.PhotoImage(file='images/ai.png')
    #username

    self.usernamelabel=Label(self.loginFrame,image=self.usernameImage,text='Username',
    compound=LEFT,font=('times new roman',20,'bold'),bg='cornflowerblue')
    self.usernamelabel.grid(row=1,column=0,padx=20,pady=10)

    self.usernameEntry=Entry(self.loginFrame,font=('times new roman',20),bd=5,fg='royalblue',textvariable=self.c_uname)
    self.usernameEntry.grid(row=1,column=1,padx=20,pady=10)

    #password
    self.passwordImage=PhotoImage(file='images/secure.png')
    self.passwordlabel=Label(self.loginFrame,image=self.passwordImage,text='Password',
    compound=LEFT,font=('times new roman',20,'bold'),bg='cornflowerblue')
    self.passwordlabel.grid(row=2,column=0,padx=20,pady=10) 

    self.passwordEntry=Entry(self.loginFrame,font=('times new roman',20),bd=5,fg='royalblue',show="*",textvariable=self.c_pwd)
    self.passwordEntry.grid(row=2,column=1,padx=20,pady=10)

    self.signupButton=Button(self.loginFrame,text="SignUp",font=('time new roman',12,'bold'),
    width=15,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2',command=self.signup)
    self.signupButton.grid(row=3,column=0,pady=10)

    self.loginButton=Button(self.loginFrame,text="Log In",font=('time new roman',12,'bold'),
    width=15,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2',command=self.logIn)
    self.loginButton.grid(row=3,column=1,pady=10)

    self.clearButton=Button(self.loginFrame,text="Clear",font=('time new roman',12,'bold'),
    width=15,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2',command=self.clearEntry)
    self.clearButton.grid(row=4,column=0,pady=10)

    self.exitButton=Button(self.loginFrame,text="Exit",font=('time new roman',12,'bold'),
    width=15,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2',command=self.exit)
    self.exitButton.grid(row=4,column=1,pady=10)

    # self.ForgetPassword=Button(self.loginFrame,text="ForgetPassword",font=('time new roman',12,'bold'),
    # width=15,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2',command=self.forgetPassword)
    # self.ForgetPassword.grid(row=5,column=0,columnspan=2,pady=10)

    
    try:
        self.con=sql.connect(database='facemaskadminreg.sqlite')
    except:
        print("Connection is not created")
    self.cursor=self.con.cursor()
    #log in
 def logIn(self):
        select="select username,password from registration where username=? and password=?"
        values=(self.usernameEntry.get(),self.passwordEntry.get())
        e=self.cursor.execute(select,values)
        resultSet=e.fetchall()
        print(resultSet)
        if(self.usernameEntry.get()=='' or self.passwordEntry.get()==''):
            messagebox.showerror('Error',"Field Can't be empty")
        elif(resultSet):
            messagebox.showinfo('Success',"Welcome To Face Mask Detctation")
            #close login window after login
            self.root.destroy()
            import facemaskdetect             
        else:
            messagebox.showerror('Error',"Please Enter correct login info")

 def signup(self):
      self.root.destroy()
      import adminreg  
 #exit
 def exit(self):
        op=messagebox.askyesno("Exit","Do you want to really Exit")
        if(op>0):
            self.root.destroy() 
 def forgetPassword(self):
        op=messagebox.askyesno("forgetPassword","Do you want to forgetPassword")
        if(op>0):
            self.root.destroy() 
            import changepassword     
#  def changepassword(self):
#     select="select username from registration where username=?"
#     values=(self.usernameEntry.get())
#     e=self.cursor.execute(select,values)
#     resultSet=e.fetchall()
#     print(resultSet)
#     if(resultSet ):
#         messagebox.showerror('Success',"Newpassword")
                     
#     else:
#         messagebox.showerror('Error',"Please Enter correct username ")
      
 
 def clearEntry(self):          
            self.usernameEntry.delete(first=0,last=100)           
            self.passwordEntry.delete(first=0,last=100)
            
            
 def error(self):
            messagebox.showerror("Error","password  not same")   
 


root=Tk()
obj=LogIn(root)
root.mainloop()