from tkinter import*

root = Tk()

username=StringVar()
password=StringVar()

# tite and background------------
root.title("Bill Book")
root.config(bg="#382D72")
root.state("zoomed")

# Title shop name----------------
entries_frames=Frame(root,bg="#382D72")
entries_frames.pack(side=TOP,fill=X)
title=Label(entries_frames,text="welcome To Kannaku Pillai📘",font=("calibri",45,"bold"),bg="#382D72" ,fg="white")
title.pack(pady=100)


#  login frame start ---------------
login_frame=Frame(root,bg="#6A6097")
login_frame.pack()

#  username ---------------
label = Label(login_frame,text="Username",font=("calibri",20,"bold"),bg="#6A6097" ,fg="white")
label.grid(row=0,column=0)
textname=Entry(login_frame,textvariable=username,font=("calibri",15),width=25)
textname.grid(row=0,column=1,pady=20 ,padx=10)

#  password ---------------
label = Label(login_frame,text="Password",font=("calibri",20,"bold"),bg="#6A6097" ,fg="white")
label.grid(row=1,column=0)
textname=Entry(login_frame,textvariable=password,font=("calibri",15),width=25)
textname.grid(row=1,column=1,pady=20 ,padx=10)

#  button ---------
# button function action------
def login():
    pass

# btn_frame=Frame(login_frame,bg="#E5CCF4")
btnlog=Button(login_frame,command=login,text="log in",bg="#E5CCF4",padx=10,pady=10,font=("calibri",15,"bold"),width=50).grid(row=3,column=0,columnspan=2)

mainloop()