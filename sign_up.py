import tkinter
from tkinter import *
from tkinter import ttk

root = Tk()

ownername=StringVar()
shopname=StringVar()
number=StringVar()
shop_id=StringVar()
email=StringVar()
branch=StringVar()
system_no=StringVar()
website=StringVar()
Username=StringVar()
Password=StringVar()
timestamp=StringVar()


# tite and background------------
root.title("Bill Book")
root.config(bg="#382D72")
root.state("zoomed")


# Title shop name----------------
entries_frames=Frame(root,bg="#382D72")
entries_frames.pack(side=TOP,fill=X)
title=Label(entries_frames,text="welcome To Bill Sheet",font=("calibri",45,"bold"),bg="#382D72" ,fg="white")
title.pack(pady=40)


#  login frame start ---------------
signup_frame=Frame(root,bg="#6A6097")
signup_frame.pack()

label_ownername = Label(signup_frame,text="ownername",font=("calibri",18,"bold"),bg="#6A6097" ,fg="white")
label_ownername.grid(row=0,column=0,padx=10,sticky="w")
textownername=Entry(signup_frame,textvariable=ownername,font=("calibri",15),width=25)
textownername.grid(row=0,column=1,pady=20,padx=15 ,sticky="w")


label_shopname = Label(signup_frame,text="Shop Name",font=("calibri",18,"bold"),bg="#6A6097" ,fg="white")
label_shopname.grid(row=0,column=2,padx=10,sticky="w")
textshopname=Entry(signup_frame,textvariable=shopname,font=("calibri",15),width=25)
textshopname.grid(row=0,column=3,pady=20,padx=15 ,sticky="w")

label_number = Label(signup_frame,text="Number",font=("calibri",18,"bold"),bg="#6A6097" ,fg="white")
label_number.grid(row=1,column=0,padx=10,sticky="w")
textnumber=Entry(signup_frame,textvariable=number,font=("calibri",15),width=25)
textnumber.grid(row=1,column=1,pady=20,padx=15 ,sticky="w")

label_shop_id = Label(signup_frame,text="Shop Id",font=("calibri",18,"bold"),bg="#6A6097" ,fg="white")
label_shop_id.grid(row=1,column=2,padx=10,sticky="w")
textshop_id=Entry(signup_frame,textvariable=shop_id,font=("calibri",15),width=25)
textshop_id.grid(row=1,column=3,pady=20,padx=15 ,sticky="w")

label_email = Label(signup_frame,text="Email",font=("calibri",18,"bold"),bg="#6A6097" ,fg="white")
label_email.grid(row=2,column=0,padx=10,sticky="w")
textemail=Entry(signup_frame,textvariable=email,font=("calibri",15),width=25)
textemail.grid(row=2,column=1,pady=20,padx=15 ,sticky="w")

label_branch = Label(signup_frame,text="Branch",font=("calibri",18,"bold"),bg="#6A6097" ,fg="white")
label_branch.grid(row=2,column=2,padx=10,sticky="w")
textbranch=Entry(signup_frame,textvariable=branch,font=("calibri",15),width=25)
textbranch.grid(row=2,column=3,pady=20,padx=15 ,sticky="w")


label_system_no = Label(signup_frame,text="System No.s",font=("calibri",18,"bold"),bg="#6A6097" ,fg="white")
label_system_no.grid(row=3,column=0,padx=10,sticky="w")
textsystem_no=Entry(signup_frame,textvariable=system_no,font=("calibri",15),width=25)
textsystem_no.grid(row=3,column=1,pady=20,padx=15 ,sticky="w")


label_website = Label(signup_frame,text="Website(url)",font=("calibri",18,"bold"),bg="#6A6097" ,fg="white")
label_website.grid(row=3,column=2,padx=10,sticky="w")
textwebsite=Entry(signup_frame,textvariable=website,font=("calibri",15),width=25)
textwebsite.grid(row=3,column=3,pady=20,padx=15 ,sticky="w")

label_Username = Label(signup_frame,text="Username",font=("calibri",18,"bold"),bg="#6A6097" ,fg="white")
label_Username.grid(row=4,column=0,padx=10,sticky="w")
textUsername=Entry(signup_frame,textvariable=Username,font=("calibri",15),width=25)
textUsername.grid(row=4,column=1,pady=20,padx=15 ,sticky="w")

label_Password = Label(signup_frame,text="Password",font=("calibri",18,"bold"),bg="#6A6097" ,fg="white")
label_Password.grid(row=4,column=2,padx=10,sticky="w")
textPassword=Entry(signup_frame,textvariable=Password,font=("calibri",15),width=25)
textPassword.grid(row=4,column=3,pady=20,padx=15 ,sticky="w")



def signup():
    pass

def exit():
    pass

# btn_frame=Frame(signup_frame,bg="#E5CCF4")
btnlog=Button(signup_frame,command=signup,text="Sign Up",bg="#E5CCF4",padx=10,pady=10,font=("calibri",15,"bold"),width=25).grid(row=6,column=1,padx=10,pady=10)
btnlog=Button(signup_frame,command=exit,text="Exit",bg="#E5CCF4",padx=10,pady=10,font=("calibri",15,"bold"),width=25).grid(row=6,column=3,padx=10,pady=10)



mainloop()