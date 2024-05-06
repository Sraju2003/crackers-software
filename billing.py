import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
name=StringVar()
ph_no=StringVar()
bill_no=StringVar()
emp_name=StringVar()
date=StringVar()
code=StringVar()
product=StringVar()
price=StringVar()
quantity=StringVar()
discount=StringVar()
amount=StringVar()


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
lablenumber=tkinter.Label(entries_frames,text="Phone No.s",font=("calibri",15),bg="#A080E1" ,fg="white")
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
lablecode=Label(bill_frame,text="Code",font=("calibri",15),bg="#E5CCF4" ,fg="black",width=10)
lablecode.grid(row=1,column=1,sticky="w")
textcode=Entry(bill_frame,textvariable=code,font=("calibri",15),width=10,)
textcode.grid(row=2,column=1,sticky="w")

# Product ----------------------
product_label = tkinter.Label(bill_frame, text="product",font=("calibri",15),bg="#E5CCF4" ,fg="black",width=30)
product_label.grid(row=1, column=2,columnspan=2)
product_entry = tkinter.Entry(bill_frame,font=("calibri",15),width=30)
product_entry.grid(row=2, column=2,columnspan=2)
# Price--------------------------
price_label = tkinter.Label(bill_frame, text="price",font=("calibri",15),bg="#E5CCF4" ,fg="black",width=20)
price_label.grid(row=1, column=4)
price_spinbox = tkinter.Spinbox(bill_frame, from_=0, to=100,font=("calibri",15),width=20)
price_spinbox.grid(row=2, column=4)

# Quantity----------------------
qty_label = tkinter.Label(bill_frame, text="Quantity",font=("calibri",15),bg="#E5CCF4" ,fg="black",width=20)
qty_label.grid(row=1, column=5)
qty_spinbox = tkinter.Spinbox(bill_frame, from_=1, to=100,font=("calibri",15),width=20)
qty_spinbox.grid(row=2, column=5)

# Discount----------------------
dis_label = tkinter.Label(bill_frame, text="Discount",font=("calibri",15),bg="#E5CCF4" ,fg="black",width=20)
dis_label.grid(row=1, column=6)
dis_entry = tkinter.Entry(bill_frame,font=("calibri",15),width=20)
dis_entry.grid(row=2, column=6)

# Amount----------------------
amount_label = tkinter.Label(bill_frame, text="Amount",font=("calibri",15),bg="#E5CCF4" ,fg="black",width=20)
amount_label.grid(row=1, column=7)
amount_spinbox = tkinter.Spinbox(bill_frame, from_=0.0, to=50000, font=("calibri",15),width=20)
amount_spinbox.grid(row=2, column=7)

#button---------------

def add_item():
    qty = int(qty_spinbox.get())
    desc = desc_entry.get()
    price = float(price_spinbox.get())
    line_total = qty*price
    invoice_item = [qty, desc, price, line_total]
    tree.insert('',0, values=invoice_item)
    clear_item()

    invoice_list.append(invoice_item)

add_item_button = tkinter.Button(bill_frame, text = "Add item", command = add_item,font=("calibri",15),bg="#E5CCF4" ,fg="black",width=10)
add_item_button.grid(row=2, column=8, pady=5)




# btn_frame=Frame(login_frame,bg="#E5CCF4")


#  
# Header space close----------------------
columns = ('desc', 'price', 'qty','dis', 'total')

style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18), rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings

tree = ttk.Treeview(bill_frame, columns=columns, show="headings")
tree.heading('qty', text='Qty')
tree.column('qty',width=20)
tree.heading('desc', text='Product')
tree.heading('price', text='Price')
tree.heading('total', text="Amount")
tree.heading('dis',text='Discount')

tree.grid(row=4, column=0, columnspan=9,padx=10)
mainloop()
