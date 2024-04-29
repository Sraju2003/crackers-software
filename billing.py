from tkinter import *

root = Tk()
name=StringVar()
ph_no=StringVar()
bill_no=StringVar()
emp_name=StringVar()
S_no=StringVar()
Product=StringVar()
Quantity=StringVar()
Discount=StringVar()
Amount=StringVar()


menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_command(label='Open')
filemenu.add_command(label='Open')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
salesmenu = Menu(menu)
menu.add_cascade(label='Sales', menu=salesmenu)
salesmenu.add_command(label='Daily Sales')
salesmenu.add_command(label='Gross Sales')
salesmenu.add_command(label='Shop-Wise')
salesmenu.add_command(label='Summary')
stockmenu = Menu(menu)
menu.add_cascade(label='Stock', menu=stockmenu)
stockmenu.add_command(label='Daily Sales')
stockmenu.add_command(label='Gross Sales')
stockmenu.add_command(label='Shop-Wise')
stockmenu.add_command(label='Summary')
reportmenu = Menu(menu)
menu.add_cascade(label='Stock', menu=reportmenu)
reportmenu.add_command(label='Daily Sales')
reportmenu.add_command(label='Gross Sales')
reportmenu.add_command(label='Shop-Wise')
reportmenu.add_command(label='Summary')

root.title("Bill Book")
root.config(bg="#382D72")
root.state("zoomed")
# customer Frame
entries_frames=Frame(root,bg="#A080E1")
entries_frames.pack(side=TOP,fill=X)
title=Label(entries_frames,text="Sales Bill",font=("calibri",20,"bold"),bg="#A080E1" ,fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=10)
# name space--------------
lablename=Label(entries_frames,text="Name",font=("calibri",15),bg="#A080E1" ,fg="white")
lablename.grid(row=1,column=1)
textname=Entry(entries_frames,textvariable=name,font=("calibri",15),width=25)
textname.grid(row=1,column=2,pady=20 ,padx=10)

# Employee space--------------
lablename=Label(entries_frames,text="Employee",font=("calibri",15),bg="#A080E1" ,fg="white")
lablename.grid(row=1,column=5)
textname=Entry(entries_frames,textvariable=emp_name,font=("calibri",15),width=25)
textname.grid(row=1,column=6 ,padx=10)

# number space--------------
lablename=Label(entries_frames,text="Phone No.s",font=("calibri",15),bg="#A080E1" ,fg="white")
lablename.grid(row=1,column=3)
textname=Entry(entries_frames,textvariable=ph_no,font=("calibri",15),width=25)
textname.grid(row=1,column=4,padx=10)

# serial number space--------------
lablename=Label(entries_frames,text="Serial No",font=("calibri",15),bg="#A080E1" ,fg="white")
lablename.grid(row=1,column=7)
textname=Entry(entries_frames,textvariable=bill_no,font=("calibri",15),width=25)
textname.grid(row=1,column=8,padx=10)

#  item bill section----------------
bill_frame=Frame(root,bg="#5C509C")
bill_frame.pack(fill=X)


# Header space----------------------
lablename=Label(bill_frame,text="S.No",font=("calibri",15),bg="#E5CCF4" ,fg="black",width=10)
lablename.grid(row=1,column=1)
textname=Entry(bill_frame,textvariable=S_no,font=("calibri",15),width=10,)
textname.grid(row=2,column=1)
# Product ----------------------
lablename=Label(bill_frame,text="Product Name",font=("calibri",15),bg="#E5CCF4" ,fg="black",width=30)
lablename.grid(row=1,column=2,columnspan=2)
textname=Entry(bill_frame,textvariable=Product,font=("calibri",15),width=30,)
textname.grid(row=2,column=2,columnspan=2)
# Quantity----------------------
lablename=Label(bill_frame,text="Quantity",font=("calibri",15),bg="#E5CCF4" ,fg="black",width=18)
lablename.grid(row=1,column=4)
textname=Entry(bill_frame,textvariable=Quantity,font=("calibri",15),width=18,)
textname.grid(row=2,column=4)
# Discount----------------------
lablename=Label(bill_frame,text="Discount",font=("calibri",15),bg="#E5CCF4" ,fg="black",width=18)
lablename.grid(row=1,column=5)
textname=Entry(bill_frame,textvariable=Discount,font=("calibri",15),width=18,)
textname.grid(row=2,column=5)
# Amount----------------------
lablename=Label(bill_frame,text="Amount",font=("calibri",15),bg="#E5CCF4" ,fg="black",width=25)
lablename.grid(row=1,column=6)
textname=Entry(bill_frame,textvariable=Amount,font=("calibri",15),width=25,)
textname.grid(row=2,column=6)
# Header space----------------------
mainloop()
