from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import sqlite3 as sql
import time
import os
import random,re,os  
class FaceMaskDetection:
    def __init__(self,root):
        #customer --------------------
        self.c_name=StringVar()
        self.name=re.compile("[a-z]+")
        self.c_mob=StringVar()
        self.mob=re.compile("[6-9]\d{9}")
        self.c_adhaar=StringVar()
        self.adhaar=re.compile("[6-9]\d{12}")
        self.c_gmail=StringVar()
        self.id_no=StringVar()
        
        random_id_no=random.randint(10000,99999)
        self.id_no.set(str(random_id_no))
        self.search_id=StringVar()
        
        self.root=root
        self.root.geometry('1280x656+0+0')
        self.root.title("FaceMask Detecation Management System")
        self.root.resizable(False,False)
        self.backgroundImage=ImageTk.PhotoImage(file='images/facemaskbg1.jpg')
        self.bgLabel=Label(self.root,image=self.backgroundImage)
        self.bgLabel.place(x=0,y=0)

        self.timeFrame=Frame(self.root)
        self.timeFrame.place(x=0,y=0)
        #time
        self.datetimeLabel=Label(self.timeFrame,font=('time new roman',14,'bold'),fg='red',bg='skyblue')
        # self.datetimeLabel.grid(x=5,y=5)
        self.datetimeLabel.grid(row=0,column=0,padx=2)
        self.clock()
        #infor
        self.signupFrame=Frame(self.root,bg ='cornflowerblue')
        self.signupFrame.place(x=750,y=100)
        #Load Image
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


        # #adhaar no
        self.adhaarImage=ImageTk.PhotoImage(file='images/adhaar.png')
        self.adhaarlabel=Label(self.signupFrame,image=self.adhaarImage,text='Adhaar No',
        compound=LEFT,font=('times new roman',20,'bold'),bg='cornflowerblue')
        self.adhaarlabel.grid(row=2,column=0,padx=20,pady=10,sticky='w')
        
        self.adhaarEntry=Entry(self.signupFrame,font=('times new roman',20),bd=5,fg='royalblue',textvariable=self.c_adhaar)
        self.adhaarEntry.grid(row=2,column=1,padx=20,pady=10)
        # #mobile no
        self.mobImage=ImageTk.PhotoImage(file='images/smartphone.png')
        self.moblabel=Label(self.signupFrame,image=self.mobImage,text='Mobile',
        compound=LEFT,font=('times new roman',20,'bold'),bg='cornflowerblue')
        self.moblabel.grid(row=3,column=0,padx=20,pady=10,sticky='w')
        
        self.mobEntry=Entry(self.signupFrame,font=('times new roman',20),bd=5,fg='royalblue',textvariable=self.c_mob)
        self.mobEntry.grid(row=3,column=1,padx=20,pady=10)
        # #gmail 
        self.gmailImage=ImageTk.PhotoImage(file='images/gmail.png')
        self.gmaillabel=Label(self.signupFrame,image=self.gmailImage,text='Gmail Id',
        compound=LEFT,font=('times new roman',20,'bold'),bg='cornflowerblue')
        self.gmaillabel.grid(row=4,column=0,padx=20,pady=10,sticky='w')

        self.gmailEntry=Entry(self.signupFrame,font=('times new roman',20),bd=5,fg='royalblue',textvariable=self.c_gmail)
        self.gmailEntry.grid(row=4,column=1,padx=20,pady=10)

        self.submitButton=Button(self.signupFrame,text="Submit",font=('time new roman',14,'bold'),
        width=15,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2',command=self.insert)
        self.submitButton.grid(row=6,column=0,pady=10)

        self.clearButton=Button(self.signupFrame,text="Clear",font=('time new roman',14,'bold'),
        width=15,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2',command=self.clearEntry)
        self.clearButton.grid(row=6,column=1,pady=10)
        #buttonframe
        self.detectFrame=Frame(self.root,bg ='cornflowerblue')
        self.detectFrame.place(x=20,y=600)

        self.searchButton=Button(self.detectFrame,text="Search",font=('time new roman',17,'bold'),
        width=8,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2')
        self.searchButton.grid(row=0,column=0,padx=10,pady=10)

        self.searchEntry=Entry(self.detectFrame,font=('times new roman',20),width=12,bd=5,fg='royalblue',textvariable=self.search_id)
        self.searchEntry.grid(row=0,column=1,padx=10,pady=10)
        # Load Image

        self.detectButton=Button(self.detectFrame,text="Mask-Detect",font=('time new roman',17,'bold'),
        width=13,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2',command=self.maskDetect)
        self.detectButton.grid(row=0,column=2,padx=10,pady=10)

        self.helpButton=Button(self.detectFrame,text="Help-Section",font=('time new roman',17,'bold'),
        width=13,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2',command=self.precautionText)
        self.helpButton.grid(row=0,column=3,padx=10,pady=10)

        self.chatButton=Button(self.detectFrame,text="Chat",font=('time new roman',17,'bold'),
        width=8,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2')
        self.chatButton.grid(row=0,column=4,padx=10,pady=10)

        self.exitButton=Button(self.detectFrame,text="Exit",font=('time new roman',17,'bold'),
        width=8,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2',command=self.exit)
        self.exitButton.grid(row=0,column=5,padx=10,pady=10)

        self.logoutButton=Button(self.detectFrame,text="Logout",font=('time new roman',17,'bold'),
        width=10,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2',command=self.logout)
        self.logoutButton.grid(row=0,column=6,padx=10,pady=10)
        try:
            self.con=sql.connect(database='facemaskadminreg.sqlite')
        except:
            messagebox.showerror("Error","Database is not created")
            
        self.cursor=self.con.cursor()
        self.cursor.execute("create table if not exists users(name varchar(30),adhaar_no char(15) primary key,mobile char(15),gmailid varchar(30))")
        
        #exit
    def exit(self):
        op=messagebox.askyesno("Exit","Do you want to really Exit")
        if(op>0):
            self.root.destroy()            
        else:
            return
            
    def clock(self):
        date=time.strftime('%d/%m/%Y')
        currenttime=time.strftime('%H:%m:%S')
        self.datetimeLabel.config(text=f'Date:{date}\nTime:{currenttime}')
        self.datetimeLabel.after(1000,self.clock)
   
    def maskDetect(self):        
         import detect_mask_video
    def precautionText(self):
        self.root.destroy()
        import login
    
    def logout(self):
        op=messagebox.askyesno("Logout","Do you want to really logout")
        if(op>0):
            self.root.destroy()
            import login
        else:
            return
    
    def clearEntry(self):
            self.nameEntry.delete(first=0,last=100)
            self.adhaarEntry.delete(first=0,last=100)
            self.mobEntry.delete(first=0,last=100)
            self.gmailEntry.delete(first=0,last=100)
            
    def error(self):
            messagebox.showerror("Error","password  not same")    
    def insert(self):
        name=self.nameEntry.get()
        adhaar=self.adhaarEntry.get()
        mob=self.mobEntry.get()
        gmail=self.gmailEntry.get()
        email="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
        #insert="insert into registration values('%s','%s','%s','%s')"%(name,user,gmail,password);
        # values=(nameEntry.get(),usernameEntry.get(),gmailEntry.get(),passwordEntry.get())
        if(name=='' or adhaar==''or mob=='' or gmail==''):
            messagebox.showwarning('Warning',"Field Can't be empty")
        
        else: 
    #         #gmail verification  
            if(re.search(email,gmail)):
              
                insertData="insert into users(name,adhaar_no,mobile,gmailid) values(?,?,?,?)"
                values=(name,adhaar,mob,gmail)
                c=self.cursor.execute(insertData,values)
                self.con.commit()        
                self.clearEntry()
                messagebox.showinfo("Database Created","your data inserted")
            else:
                messagebox.showwarning('Warning',"Wrong Email Id")

    # def findBill(self):
    #     present='no'
    #     d=os.listdir("bill/")
        
    #     for i in d:
    #         if(i.split('.')[0]==self.search_id.get()):
    #           file=open(f"ids/{i}","r")  
    #           self.txtarea.delete('1.0',END)
    #           for d in file:
    #             self.txtarea.insert(END,d)
    #           file.close()
    #           present='yes'
    #     if(present=='no' ):
    #         messagebox.showerror("Error","Invalid No.")
root=Tk()
FaceMask=FaceMaskDetection(root)
root.mainloop()