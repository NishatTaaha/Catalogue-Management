from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1100x500+220+130')
        self.root.title('Inventory Mamagement System')
        self.root.config(bg='white')
        self.root.focus_force()

        ########### all variables ############
        self.var_searchby = StringVar()
        self.var_searchText = StringVar()
        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_usertype = StringVar()
        self.var_salary = StringVar()

        ########### search frame ############
        searchFrame = LabelFrame(self.root, text='Search Employee', bg='white', relief=RIDGE,
                                 font=('goudy old style', 12, 'bold'), bd=2)
        searchFrame.place(x=250, y=20, width=600, height=70)

        ########### options ############
        cmb_search = ttk.Combobox(searchFrame, textvariable=self.var_searchby,
                                  values=('Select', 'Email', 'Name', 'Contact'), state='readonly',
                                  font=('goudy old style', 12))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(searchFrame, textvariable=self.var_searchText, font=('goudy old style', 15),
                           bg='lightyellow').place(x=200, y=10)
        btn_search = Button(searchFrame, text='Search', font=('goudy old style', 15, 'bold'), bg='maroon', fg='white',
                            cursor='hand2', command=self.search).place(x=430, y=9, width=130, height=30)

        ########### title ############
        title = Label(self.root, text='Employee Details', font=('goudy old style', 15), bg='darkblue', fg='white',
                      cursor='hand2').place(x=50, y=100, width=1000)

        ########### content ############
        # row1
        lbl_emp_id = Label(self.root, text='Emp ID', font=('goudy old style', 15), bg='white').place(x=50, y=150)
        lbl_gender = Label(self.root, text='Gender', font=('goudy old style', 15), bg='white').place(x=350, y=150)
        lbl_contact = Label(self.root, text='Contact', font=('goudy old style', 15), bg='white').place(x=750, y=150)
        txt_emp_id = Entry(self.root, textvariable=self.var_emp_id, font=('goudy old style', 15),
                           bg='lightyellow').place(x=150, y=150, width=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=('Select', 'Male', 'Female', 'Other'),
                                  state='readonly', font=('goudy old style', 12))
        cmb_gender.place(x=500, y=150, width=180, height=28)
        cmb_gender.current(0)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=('goudy old style', 15),
                            bg='lightyellow').place(x=850, y=150, width=180)

        # row2
        lbl_name = Label(self.root, text='Name', font=('goudy old style', 15), bg='white').place(x=50, y=190)
        lbl_dob = Label(self.root, text='D.O.B', font=('goudy old style', 15), bg='white').place(x=350, y=190)
        lbl_doj = Label(self.root, text='D.O.J', font=('goudy old style', 15), bg='white').place(x=750, y=190)
        txt_name = Entry(self.root, textvariable=self.var_name, font=('goudy old style', 15), bg='lightyellow').place(
            x=150, y=190, width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=('goudy old style', 15), bg='lightyellow').place(
            x=500, y=190, width=180)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=('goudy old style', 15), bg='lightyellow').place(
            x=850, y=190, width=180)

        # row3
        lbl_email = Label(self.root, text='Email', font=('goudy old style', 15), bg='white').place(x=50, y=230)
        lbl_password = Label(self.root, text='Password', font=('goudy old style', 15), bg='white').place(x=350, y=230)
        lbl_usertype = Label(self.root, text='Usertype', font=('goudy old style', 15), bg='white').place(x=750, y=230)
        txt_email = Entry(self.root, textvariable=self.var_email, font=('goudy old style', 15), bg='lightyellow').place(
            x=150, y=230, width=180)
        txt_password = Entry(self.root, textvariable=self.var_pass, font=('goudy old style', 15),
                             bg='lightyellow').place(x=500, y=230, width=180)
        cmb_usertype = ttk.Combobox(self.root, textvariable=self.var_usertype, values=('Admin', 'Employee'),
                                    state='readonly', font=('goudy old style', 12))
        cmb_usertype.place(x=850, y=230, width=180, height=28)
        cmb_usertype.current(0)

        # row4
        lbl_address = Label(self.root, text='Address', font=('goudy old style', 15), bg='white').place(x=50, y=270)
        lbl_salary = Label(self.root, text='Salary', font=('goudy old style', 15), bg='white').place(x=500, y=270)
        self.txt_address = Text(self.root, font=('goudy old style', 15), bg='lightyellow')
        self.txt_address.place(x=150, y=270, width=300, height=60)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=('goudy old style', 15),
                           bg='lightyellow').place(x=600, y=270, width=180)

        ########### buttons ############
        btn_add = Button(self.root, text='Save', font=('goudy old style', 15), bg='maroon', fg='white', cursor='hand2',
                         command=self.add).place(x=500, y=305, width=110, height=28)
        btn_update = Button(self.root, text='Update', font=('goudy old style', 15), bg='darkblue', fg='white',
                            cursor='hand2', command=self.update).place(x=620, y=305, width=110, height=28)
        btn_delete = Button(self.root, text='Delete', font=('goudy old style', 15), bg='purple', fg='white',
                            cursor='hand2', command=self.delete).place(x=740, y=305, width=110, height=28)
        btn_clear = Button(self.root, text='Clear', font=('goudy old style', 15), bg='darkgreen', fg='white',
                           cursor='hand2', command=self.clear).place(x=860, y=305, width=110, height=28)

        ########### employee details ############
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.employeeTable = ttk.Treeview(emp_frame, column=(
        'eid', 'name', 'email', 'gender', 'contact', 'dob', 'doj', 'pass', 'utype', 'address', 'salary'),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrolly.config(command=self.employeeTable.yview)
        scrollx.config(command=self.employeeTable.xview)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)

        self.employeeTable.heading('eid', text='EMP ID')
        self.employeeTable.heading('name', text='Name')
        self.employeeTable.heading('email', text='Email')
        self.employeeTable.heading('gender', text='Gender')
        self.employeeTable.heading('contact', text='Contact')
        self.employeeTable.heading('dob', text='D.O.B')
        self.employeeTable.heading('doj', text='D.O.J')
        self.employeeTable.heading('pass', text='Password')
        self.employeeTable.heading('utype', text='User Type')
        self.employeeTable.heading('address', text='Address')
        self.employeeTable.heading('salary', text='Salary')

        self.employeeTable['show'] = 'headings'

        self.employeeTable.column('eid', width=90)
        self.employeeTable.column('name', width=100)
        self.employeeTable.column('email', width=100)
        self.employeeTable.column('gender', width=100)
        self.employeeTable.column('contact', width=100)
        self.employeeTable.column('dob', width=100)
        self.employeeTable.column('doj', width=100)
        self.employeeTable.column('pass', width=100)
        self.employeeTable.column('utype', width=100)
        self.employeeTable.column('address', width=100)
        self.employeeTable.column('salary', width=100)
        self.employeeTable.pack(fill=BOTH, expand=1)
        self.employeeTable.bind('<ButtonRelease-1>', self.get_data)

        self.show()

    #################################
    def add(self):
        con = sqlite3.connect(database='taaha.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == '':
                messagebox.showerror('Error', 'Employee ID must be required!', parent=self.root)
            else:
                cur.execute('Select * from employee where  eid=?', (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror('Error', 'This Employee ID already assigned!', parent=self.root)

                else:
                    cur.execute(
                        'Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)',
                        (
                            self.var_emp_id.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_usertype.get(),
                            self.txt_address.get('1.0', END),
                            self.var_salary.get(),
                        ))
                    con.commit()
                    messagebox.showinfo('Success', 'Employee Added Successfully!!')
                    self.clear()
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to : {str(ex)}', parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'taaha.db')
        cur = con.cursor()
        try:
            cur.execute('select * from employee')
            rows = cur.fetchall()
            self.employeeTable.delete(*self.employeeTable.get_children())
            for row in rows:
                self.employeeTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to : {str(ex)}', parent=self.root)

    def get_data(self, ev):
        f = self.employeeTable.focus()
        content = (self.employeeTable.item(f))
        row = content['values']
        # print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_usertype.set(row[8])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[9])
        self.var_salary.set(row[10])

    def update(self):
        con = sqlite3.connect(database='taaha.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == '':
                messagebox.showerror('Error', 'Employee ID must be required!', parent=self.root)
            else:
                cur.execute('Select * from employee where  eid=?', (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Invalid Employee ID', parent=self.root)

                else:
                    cur.execute(
                        'Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?',
                        (
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_usertype.get(),
                            self.txt_address.get('1.0', END),
                            self.var_salary.get(),
                            self.var_emp_id.get(),
                        ))
                    con.commit()
                    messagebox.showinfo('Success', 'Employee Updated Successfully!!')
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to : {str(ex)}', parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'taaha.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == '':
                messagebox.showerror('Error', 'Employee ID must be required!')
            else:
                cur.execute('Select * from employee where eid=?', (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Invalid Employee ID!', parent=self.root)

                else:
                    op = messagebox.askyesno('Confirm', 'Do you really want to delete?', parent=self.root)
                    if op == True:
                        cur.execute('delete from employee where eid=?', (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo('Delete', 'Employee Deleted Successfully!')
                        self.var_emp_id.set('')
                        self.var_name.set('')
                        self.var_email.set('')
                        self.var_gender.set('')
                        self.var_contact.set('')
                        self.var_dob.set('')
                        self.var_doj.set('')
                        self.var_pass.set('')
                        self.var_usertype.set('')
                        self.txt_address.delete('1.0', END)
                        self.var_salary.set('')
                        self.var_searchText.set('')
                        self.show()

        except Exception as ex:
            messagebox.showerror('Error', f'Error due to : {str(ex)}', parent=self.root)

    def clear(self):
        self.var_emp_id.set('')
        self.var_name.set('')
        self.var_email.set('')
        self.var_gender.set('Select')
        self.var_contact.set('')
        self.var_dob.set('')
        self.var_doj.set('')
        self.var_pass.set('')
        self.var_usertype.set('Admin')
        self.txt_address.delete('1.0', END)
        self.var_salary.set('')
        self.var_searchText.set('')
        self.show()

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
                    "select * from employee where " + self.var_searchby.get() + " LIKE '%" + self.var_searchText.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.employeeTable.delete(*self.employeeTable.get_children())
                    for row in rows:
                        self.employeeTable.insert('', END, values=row)
                else:
                    messagebox.showerror('Error', 'No record found!!', parent=self.root)

        except Exception as ex:
            messagebox.showerror('Error', f'Error due to : {str(ex)}', parent=self.root)


if __name__ == '__main__':
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()