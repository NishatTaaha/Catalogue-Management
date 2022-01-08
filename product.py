from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1100x500+220+130')
        self.root.title('Inventory Management System')
        self.root.config(bg='white')
        self.root.focus_force()

        ########### all variables ############
        self.var_pid = StringVar()
        self.var_category = StringVar()
        self.var_supplier = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()
        self.var_searchby = StringVar()
        self.var_searchText = StringVar()

        ########### left frame ############
        leftFrame = Frame(self.root, bd=2, relief=RIDGE).place(x=20, y=20, width=430, height=450)
        leftTitle = Label(leftFrame, text='Manage Product Details', font=('goudy old style', 15), bg='darkblue',
                          fg='white').place(x=20, y=20, width=430, height=40)

        lbl_category = Label(leftFrame, text='Category', font=('goudy old style', 15)).place(x=40, y=75)
        cmb_category = ttk.Combobox(self.root, textvariable=self.var_category,
                                    values=('Select', 'Television', 'Mobile', 'Grocery'), state='readonly',
                                    font=('goudy old style', 12))
        cmb_category.place(x=150, y=80)
        cmb_category.current(0)

        lbl_supplier = Label(leftFrame, text='Supplier', font=('goudy old style', 15)).place(x=40, y=130)
        cmb_supplier = ttk.Combobox(self.root, textvariable=self.var_supplier,
                                    values=('Select', 'Supplier 1', 'Supplier 2', 'Supplier 3'), state='readonly',
                                    font=('goudy old style', 12))
        cmb_supplier.place(x=150, y=130)
        cmb_supplier.current(0)

        lbl_name = Label(leftFrame, text='Name', font=('goudy old style', 15)).place(x=40, y=185)
        txt_name = Entry(leftFrame, textvariable=self.var_name, font=('goudy old style', 15), bg='lightyellow').place(
            x=150, y=185)

        lbl_price = Label(leftFrame, text='Price', font=('goudy old style', 15)).place(x=40, y=240)
        txt_price = Entry(leftFrame, textvariable=self.var_price, font=('goudy old style', 15), bg='lightyellow').place(
            x=150, y=240)

        lbl_QTY = Label(leftFrame, text='QTY', font=('goudy old style', 15)).place(x=40, y=295)
        txt_QTY = Entry(leftFrame, textvariable=self.var_qty, font=('goudy old style', 15), bg='lightyellow').place(
            x=150, y=295)

        lbl_status = Label(leftFrame, text='Status', font=('goudy old style', 15)).place(x=40, y=350)
        cmb_status = ttk.Combobox(self.root, textvariable=self.var_status,
                                  values=('Active', 'Dalily', 'Monthly', 'Yearly'), state='readonly',
                                  font=('goudy old style', 12))
        cmb_status.place(x=150, y=355)
        cmb_status.current(0)

        ########### buttons ############
        btn_add = Button(leftFrame, text='Save', font=('goudy old style', 15), bg='maroon', fg='white',
                         cursor='hand2', command=self.add).place(x=30, y=410, width=90, height=31)
        btn_update = Button(leftFrame, text='Update', font=('goudy old style', 15), bg='darkblue', fg='white',
                            cursor='hand2', command=self.update).place(x=125, y=410, width=90, height=31)
        btn_delete = Button(leftFrame, text='Delete', font=('goudy old style', 15), bg='purple', fg='white',
                            cursor='hand2', command=self.delete).place(x=220, y=410, width=90, height=31)
        btn_clear = Button(leftFrame, text='Clear', font=('goudy old style', 15), bg='darkgreen', fg='white',
                           cursor='hand2', command=self.clear).place(x=315, y=410, width=90, height=31)

        ########### search frame ############
        searchFrame = LabelFrame(self.root, text='Search Employee', bg='white', relief=RIDGE,
                                 font=('goudy old style', 12, 'bold'), bd=2)
        searchFrame.place(x=480, y=10, width=600, height=80)

        ########### search options ############
        cmb_search = ttk.Combobox(searchFrame, textvariable=self.var_searchby,
                                  values=('Select', 'Category', 'Supplier', 'Name'), state='readonly',
                                  font=('goudy old style', 12))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(searchFrame, textvariable=self.var_searchText, font=('goudy old style', 15),
                           bg='lightyellow').place(x=200, y=10)
        btn_search = Button(searchFrame, text='Search', font=('goudy old style', 15, 'bold'), bg='maroon', fg='white',
                            cursor='hand2').place(x=430, y=9, width=130, height=30)

        ########### employee details ############
        product_frame = Frame(self.root, bd=3, relief=RIDGE)
        product_frame.place(x=480, y=100, width=600, height=390)

        scrolly = Scrollbar(product_frame, orient=VERTICAL)
        scrollx = Scrollbar(product_frame, orient=HORIZONTAL)

        self.productTable = ttk.Treeview(product_frame, column=(
            'pid', 'Category', 'Supplier', 'Name', 'Price', 'Qty', 'Status'),
                                         yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrolly.config(command=self.productTable.yview)
        scrollx.config(command=self.productTable.xview)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)

        self.productTable.heading('pid', text='pid')
        self.productTable.heading('Category', text='Category')
        self.productTable.heading('Supplier', text='Supplier')
        self.productTable.heading('Name', text='Name')
        self.productTable.heading('Price', text='Price')
        self.productTable.heading('Qty', text='Qty')
        self.productTable.heading('Status', text='Status')

        self.productTable['show'] = 'headings'

        self.productTable.column('pid', width=90)
        self.productTable.column('Category', width=100)
        self.productTable.column('Supplier', width=100)
        self.productTable.column('Name', width=100)
        self.productTable.column('Price', width=100)
        self.productTable.column('Qty', width=100)
        self.productTable.column('Status', width=100)

        self.productTable.pack(fill=BOTH, expand=1)
        self.productTable.bind('<ButtonRelease-1>', self.get_data)

        self.show()

    # #################################

    ######### add function #########
    def add(self):
        con = sqlite3.connect(database='taaha.db')
        cur = con.cursor()
        try:
            if self.var_category.get() == 'Select' or self.var_category.get() == 'Empty' or self.var_supplier.get() == 'Select' or self.var_name.get() == '':
                messagebox.showerror('Error', 'All fields are required!!', parent=self.root)
            else:
                cur.execute('Select * from product where  name=?', (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror('Error', 'Product already present! Try different!!!', parent=self.root)

                else:
                    cur.execute(
                        'Insert into product (Category,Supplier,Name,Price,Qty,Status) values(?,?,?,?,?,?)',
                        (
                            self.var_category.get(),
                            self.var_supplier.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                        ))
                    con.commit()
                    messagebox.showinfo('Success', 'Product Added Successfully!!')
                    self.var_category.set('')
                    self.var_supplier.set('')
                    self.var_name.set('')
                    self.var_price.set('')
                    self.var_qty.set('')
                    self.var_status.set('')
                    self.var_pid.set('')
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to : {str(ex)}', parent=self.root)

    ######### show function #########
    def show(self):
        con = sqlite3.connect(database=r'taaha.db')
        cur = con.cursor()
        try:
            cur.execute('select * from product')
            rows = cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to : {str(ex)}', parent=self.root)

    ######### get data function #########
    def get_data(self, ev):
        f = self.productTable.focus()
        content = (self.productTable.item(f))
        row = content['values']
        # print(row)
        self.var_pid.set(row[0])
        self.var_category.set(row[1])
        self.var_supplier.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])

    ######## update function#########
    def update(self):
        con = sqlite3.connect(database='taaha.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == '':
                messagebox.showerror('Error', 'Please select product from list', parent=self.root)
            else:
                cur.execute('Select * from product where  pid=?', (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Invalid Product ID', parent=self.root)

                else:
                    cur.execute(
                        'Update product set Category=?,Supplier=?,Name=?,Price=?,Qty=?,Status=? where pid=?',
                        (
                            self.var_category.get(),
                            self.var_supplier.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                            self.var_pid.get()
                        ))
                    con.commit()
                    messagebox.showinfo('Success', 'Product Updated Successfully!!')
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to : {str(ex)}', parent=self.root)

    ########### delete function ############
    def delete(self):
        con = sqlite3.connect(database=r'taaha.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == '':
                messagebox.showerror('Error', 'Product ID must be required!')
            else:
                cur.execute('Select * from product where pid=?', (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Invalid Product ID!', parent=self.root)

                else:
                    op = messagebox.askyesno('Confirm', 'Do you really want to delete?', parent=self.root)
                    if op == True:
                        cur.execute('delete from product where pid=?', (self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo('Delete', 'Product Deleted Successfully!')
                        self.var_category.set('')
                        self.var_supplier.set('')
                        self.var_name.set('')
                        self.var_price.set('')
                        self.var_qty.set('')
                        self.var_status.set('')
                        self.var_pid.set('')
                        self.show()

        except Exception as ex:
            messagebox.showerror('Error', f'Error due to : {str(ex)}', parent=self.root)

    def clear(self):
        self.var_category.set('')
        self.var_supplier.set('')
        self.var_name.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.var_status.set('')
        self.var_pid.set('')
        self.show()

    ############ search function ############
    def search(self):
        con = sqlite3.connect(database='taaha.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == 'Select':
                messagebox.showerror('Error', 'Select search by option!', parent=self.root)
            elif self.var_searchby.get() == '':
                messagebox.showerror('Error', 'Select input should required!', parent=self.root)
            else:
                cur.execute(
                    "select * from product where " + self.var_searchby.get() + " LIKE '%" + self.var_searchText.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('', END, values=row)
                else:
                    messagebox.showerror('Error', 'No record found!!', parent=self.root)

        except Exception as ex:
            messagebox.showerror('Error', f'Error due to : {str(ex)}', parent=self.root)


if __name__ == '__main__':
    root = Tk()
    obj = productClass(root)
    root.mainloop()
