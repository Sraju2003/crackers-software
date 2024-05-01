from tkinter import *
from tkinter import ttk

root = Tk()
name=StringVar()
ph_no=StringVar()
bill_no=StringVar()
emp_name=StringVar()
date=StringVar()
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
lablename.grid(row=1,column=1,sticky="w")
textname=Entry(entries_frames,textvariable=name,font=("calibri",15),width=25)
textname.grid(row=1,column=2,pady=20 ,padx=10,sticky="w")

# Employee space--------------
lableEmployee=Label(entries_frames,text="Employee",font=("calibri",15),bg="#A080E1" ,fg="white")
lableEmployee.grid(row=1,column=3,sticky="w")
comboEmployee=ttk.Combobox(entries_frames,font=("calibri",15),width=25,textvariable=emp_name,state="readonly")
comboEmployee['values']=("raju","suresh","muthu","rajaesh","malini",)
comboEmployee.grid(row=1,column=4 ,padx=10,sticky="w")

#date box---------------------
labledate=Label(entries_frames,text="Date",font=("calibri",15),bg="#A080E1" ,fg="white")
labledate.grid(row=1,column=5,sticky="w")
textdate=Entry(entries_frames,textvariable=date,font=("calibri",15),width=25)
textdate.grid(row=1,column=6 ,padx=10,sticky="w")

# number space--------------
lablenumber=Label(entries_frames,text="Phone No.s",font=("calibri",15),bg="#A080E1" ,fg="white")
lablenumber.grid(row=2,column=1,sticky="w")
textnumber=Entry(entries_frames,textvariable=ph_no,font=("calibri",15),width=25)
textnumber.grid(row=2,column=2,padx=10,sticky="w" ,pady=10)

# serial number space--------------
lablebill_no=Label(entries_frames,text="Bill No",font=("calibri",15),bg="#A080E1" ,fg="white")
lablebill_no.grid(row=1,column=7,sticky="w")
textbill_no=Entry(entries_frames,textvariable=bill_no,font=("calibri",15),width=25)
textbill_no.grid(row=1,column=8,padx=10,sticky="w")

#  item bill section----------------
bill_frame=Frame(root,bg="#5C509C")
bill_frame.pack(fill=X)


# Header space opens----------------------
lableS_no=Label(bill_frame,text="S.No",font=("calibri",15),bg="#E5CCF4" ,fg="black",width=10)
lableS_no.grid(row=1,column=1,sticky="w")
textS_no=Entry(bill_frame,textvariable=S_no,font=("calibri",15),width=10,)
textS_no.grid(row=2,column=1,sticky="w")

# Product ----------------------
lableproduct=Label(bill_frame,text="Product Name",font=("calibri",15),bg="#E5CCF4" ,fg="black",width=30)
lableproduct.grid(row=1,column=2,columnspan=2,sticky="w")
textproduct=Entry(bill_frame,textvariable=Product,font=("calibri",15),width=30,)
textproduct.grid(row=2,column=2,columnspan=2,sticky="w")

# Quantity----------------------
lableqyantity=Label(bill_frame,text="Quantity",font=("calibri",15),bg="#E5CCF4" ,fg="black",width=18)
lableqyantity.grid(row=1,column=4,sticky="w")
textqyantity=Entry(bill_frame,textvariable=Quantity,font=("calibri",15),width=18,)
textqyantity.grid(row=2,column=4,sticky="w")

# Discount----------------------
lablediscount=Label(bill_frame,text="Discount",font=("calibri",15),bg="#E5CCF4" ,fg="black",width=18)
lablediscount.grid(row=1,column=5,sticky="w")
textdiscount=Entry(bill_frame,textvariable=Discount,font=("calibri",15),width=18,)
textdiscount.grid(row=2,column=5,sticky="w")

# Amount----------------------
lableamount=Label(bill_frame,text="Amount",font=("calibri",15),bg="#E5CCF4" ,fg="black",width=25)
lableamount.grid(row=1,column=6,sticky="w")
textamount=Entry(bill_frame,textvariable=Amount,font=("calibri",15),width=25,)
textamount.grid(row=2,column=6,sticky="w")

#button---------------
def add():
    pass

# btn_frame=Frame(login_frame,bg="#E5CCF4")
btnlog=Button(bill_frame,command=add,text="Add_Items",bg="#E5CCF4",font=("calibri",15),width=25).grid(row=2,column=7,pady=1,padx=10)

# Header space close----------------------

# Table Frame
table_frame= Frame(root,bg="#B7C2C6")
table_frame.place(x=20,y=250,width=1500,height=450)
style= ttk.Style()
style.configure("mystyle.Treeview.", font=('calibri',14,),rowheight=50)
style.configure("mystyle.Treeview.Heading", font=('calibri',16),)
#modify font of the body-------------
tv=ttk.Treeview(table_frame,columns=(1,2,3,4,5),style="mystyle.Treeview")
tv.heading("1",text="S_no")
tv.column("1",width=10)
tv.heading("2",text="Product")
tv.heading("3",text="Quantity")
tv.column("3",width=10)
tv.heading("4",text="Discount")
tv.column("4",width=10)
tv.heading("5",text="Amount")
tv.column("5",width=20)
tv['show']='headings'
tv.pack(fill=X)


mainloop()
