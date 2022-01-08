from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1100x500+220+130')
        self.root.title('Inventory Mamagement System')
        self.root.config(bg='white')
        self.root.focus_force()

        ############# variables ##############
        self.var_cat=StringVar()
        self.var_name=StringVar()

        ############# title ##############
        lbl_title=Label(self.root,text='Manage Product Category',font=('goudy old style',30),bg='#682B73',fg='white',bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)

        lbl_name=Label(self.root,text='Enter Category Name',font=('goudy old style',30),bg='white').place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=('goudy old style',18),bg='lightyellow').place(x=50,y=170,width=300)


        ############# button ##############
        btn_add=Button(self.root,text='Add',font=('goudy old style',15),bg='purple',fg='white',cursor='hand2',command=self.add).place(x=360,y=170,width=150,height=32)
        btn_delete=Button(self.root,text='Delete',font=('goudy old style',15),bg='green',fg='white',cursor='hand2',command=self.delete).place(x=520,y=170,width=150,height=32)


        ########### category details ############
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=100)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.categoryTable=ttk.Treeview(cat_frame,column=('cid','name'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrolly.config(command=self.categoryTable.yview)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)

        self.categoryTable.heading('cid',text='C ID')
        self.categoryTable.heading('name',text='Name')

        self.categoryTable['show']='headings'

        self.categoryTable.column('cid',width=90)
        self.categoryTable.column('name',width=100)
        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.bind('<ButtonRelease-1>',self.get_data)


        ############ images #############
        self.im1=Image.open('images/Business Plan-pana.png')
        self.im1=self.im1.resize((400,300),Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(self.im1)
        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=50,y=220)

        self.im2=Image.open('images/Community-amico.png')
        self.im2=self.im2.resize((400,300),Image.ANTIALIAS)
        self.im2=ImageTk.PhotoImage(self.im2)
        self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=580,y=220)

        self.show()

    ###################################################

    def add(self):
        con=sqlite3.connect(database='taaha.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=='':
                messagebox.showerror('Error','Category name must be required!',parent=self.root)
            else:
                cur.execute('Select * from category where name=?',(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error','Category already present!',parent=self.root)

                else:
                    cur.execute('Insert into category (name) values(?)',(
                        self.var_name.get(),
                    ))
                    con.commit()
                    messagebox.showinfo('Success','Supplier Added Successfully!!')
                    # self.clear()
                    # self.show()
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)




    def show(self):
        con=sqlite3.connect(database=r'taaha.db')
        cur=con.cursor()
        try:
            cur.execute('select * from category')
            rows=cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to : {str(ex)}', parent=self.root)



    def get_data(self,ev):
        f=self.categoryTable.focus()
        content=(self.categoryTable.item(f))
        row=content['values']
        # print(row)
        self.var_cat.set(row[0])
        self.var_name.set(row[1])



    def delete(self):
        con=sqlite3.connect(database=r'taaha.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=='':
                messagebox.showerror('Error','Please select category from the list!')
            else:
                cur.execute('Select * from category where cid=?',(self.var_cat.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Error, Please try again!',parent=self.root)

                else:
                    op=messagebox.askyesno('Confirm','Do you really want to delete?',parent=self.root)
                    if op==True:
                        cur.execute('delete from category where cid=?',(self.var_cat.get(),))
                        con.commit()
                        messagebox.showinfo('Delete','Category Deleted Successfully!')
                        self.show()
                        self.var_cat.set('')
                        self.var_name.set('')


        except Exception as ex:
            messagebox.showerror('Error', f'Error due to : {str(ex)}', parent=self.root)




if __name__=='__main__':
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()

