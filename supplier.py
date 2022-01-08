from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1100x500+220+130')
        self.root.title('Inventory Mamagement System')
        self.root.config(bg='white')
        self.root.focus_force()

        ########### all variables ############
        self.var_searchby=StringVar()
        self.var_searchText=StringVar()
        self.var_supplier_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()



        ########### search frame ############
        # searchFrame=LabelFrame(self.root,text='Search Employee',bg='white',relief=RIDGE,font=('goudy old style',12,'bold'),bd=2)
        # searchFrame.place(x=170,y=20,width=700,height=70)

        ########### label search ############
        lbl_search=Label(self.root,text='Invoice No',bg='white',font=('goudy old style',15))
        lbl_search.place(x=700,y=80)

        txt_search=Entry(self.root,textvariable=self.var_searchText,font=('goudy old style',15),bg='lightyellow').place(x=800,y=80,width=170)
        btn_search = Button(self.root,text='Search',font=('goudy old style',15,'bold'), bg='maroon',fg='white',cursor='hand2',command=self.search).place(x=980, y=79,width=100,height=30)

        ########### title ############
        title = Label(self.root,text='Supplier Details',font=('goudy old style',20,'bold'), bg='darkblue',fg='white',cursor='hand2').place(x=50, y=10,width=1000,height=40)

        ########### content ############
        # row1
        lbl_supplier_invoice = Label(self.root,text='Invoice No.',font=('goudy old style',15), bg='white').place(x=50, y=80)
        txt_supplier_invoice = Entry(self.root,textvariable=self.var_supplier_invoice,font=('goudy old style',15), bg='lightyellow').place(x=180, y=80,width=180)

        lbl_name = Label(self.root,text='Name',font=('goudy old style',15), bg='white').place(x=50, y=120)
        txt_name = Entry(self.root,textvariable=self.var_name,font=('goudy old style',15), bg='lightyellow').place(x=180, y=120,width=180)

        lbl_contact = Label(self.root,text='Contact',font=('goudy old style',15), bg='white').place(x=50, y=160)
        txt_contact = Entry(self.root,textvariable=self.var_contact,font=('goudy old style',15), bg='lightyellow').place(x=180, y=160,width=180)

        lbl_description = Label(self.root,text='Description',font=('goudy old style',15), bg='white').place(x=50, y=200)
        self.txt_description = Text(self.root,font=('goudy old style',15), bg='lightyellow')
        self.txt_description.place(x=180, y=200,width=370,height=90)

        ########### buttons ############
        btn_add=Button(self.root,text='Save',font=('goudy old style',15),bg='maroon',fg='white',cursor='hand2',command=self.add).place(x=100, y=370,width=120,height=45)
        btn_update=Button(self.root,text='Update',font=('goudy old style',15),bg='darkblue',fg='white',cursor='hand2',command=self.update).place(x=250, y=370,width=120,height=45)
        btn_delete=Button(self.root,text='Delete',font=('goudy old style',15),bg='purple',fg='white',cursor='hand2',command=self.delete).place(x=400, y=370,width=120,height=45)
        btn_clear=Button(self.root,text='Clear',font=('goudy old style',15),bg='darkgreen',fg='white',cursor='hand2',command=self.clear).place(x=550, y=370,width=120,height=45)



        ########### employee details ############
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=120,width=380,height=350)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(emp_frame,column=('invoice','name','contact','desc'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrolly.config(command=self.supplierTable.yview)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)

        self.supplierTable.heading('invoice',text='Invoice No')
        self.supplierTable.heading('name',text='Name')
        self.supplierTable.heading('contact',text='Contact')
        self.supplierTable.heading('desc',text='Description')

        self.supplierTable['show']='headings'

        self.supplierTable.column('invoice',width=90)
        self.supplierTable.column('name',width=100)
        self.supplierTable.column('contact',width=100)
        self.supplierTable.column('desc',width=100)
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind('<ButtonRelease-1>',self.get_data)

        self.show()
    #################################
    def add(self):
        con=sqlite3.connect(database='taaha.db')
        cur=con.cursor()
        try:
            if self.var_supplier_invoice.get()=='':
                messagebox.showerror('Error','Invoice must be required!',parent=self.root)
            else:
                cur.execute('Select * from supplier where  invoice=?',(self.var_supplier_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error','Invoice No. already assigned!',parent=self.root)

                else:
                    cur.execute('Insert into supplier (invoice,name,contact,desc) values(?,?,?,?)',(
                        self.var_supplier_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_description.get('1.0',END)
                    ))
                    con.commit()
                    messagebox.showinfo('Success','Supplier Added Successfully!!')
                    self.clear()
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r'taaha.db')
        cur=con.cursor()
        try:
            cur.execute('select * from supplier')
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to : {str(ex)}', parent=self.root)



    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        # print(row)
        self.var_supplier_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[3])

    def update(self):
        con = sqlite3.connect(database='taaha.db')
        cur = con.cursor()
        try:
            if self.var_supplier_invoice.get() == '':
                messagebox.showerror('Error', 'Invoice No. must be required!', parent=self.root)
            else:
                cur.execute('Select * from supplier where  invoice=?', (self.var_supplier_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Invalid Invoice No.', parent=self.root)

                else:
                    cur.execute(
                        'Update supplier set name=?,contact=?,desc=? where invoice=?',(
                            self.var_name.get(),
                            self.var_contact.get(),
                            self.txt_description.get('1.0', END),
                            self.var_supplier_invoice.get(),
                        ))
                    con.commit()
                    messagebox.showinfo('Success', 'Supplier Updated Successfully!!')
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to : {str(ex)}', parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'taaha.db')
        cur=con.cursor()
        try:
            if self.var_supplier_invoice.get()=='':
                messagebox.showerror('Error','Invoice No. must be required!')
            else:
                cur.execute('Select * from supplier where invoice=?',(self.var_supplier_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Invalid Invoice No.!',parent=self.root)

                else:
                    op=messagebox.askyesno('Confirm','Do you really want to delete?',parent=self.root)
                    if op==True:
                        cur.execute('delete from supplier where invoice=?',(self.var_supplier_invoice.get(),))
                        con.commit()
                        messagebox.showinfo('Delete','Supplier Deleted Successfully!')
                        self.var_supplier_invoice.set('')
                        self.var_name.set('')
                        self.var_contact.set('')
                        self.txt_description.delete('1.0', END)
                        self.var_searchText.set('')
                        self.show()

        except Exception as ex:
            messagebox.showerror('Error', f'Error due to : {str(ex)}', parent=self.root)


    def clear(self):
        self.var_supplier_invoice.set('')
        self.var_name.set('')
        self.var_contact.set('')
        self.txt_description.delete('1.0',END)
        self.var_searchText.set('')
        self.show()

    def search(self):
        con=sqlite3.connect(database='taaha.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=='':
                messagebox.showerror('Error', 'Invoice No. should required!', parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchText.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror('Error','No record found!!',parent=self.root)

        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)

if __name__=='__main__':
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()