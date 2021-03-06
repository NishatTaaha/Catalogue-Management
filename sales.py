from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os


class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1100x500+220+130')
        self.root.title('Inventory Mamagement System')
        self.root.config(bg='white')
        self.root.focus_force()
        self.bill_list = []

        ########## all variables ##########
        self.var_invoice = StringVar()

        ########### title ############
        lbl_title = Label(self.root, text='View Customer Bills', font=('goudy old style', 25), bg='#92E3A9',
                          fg='black', bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)

        lbl_invoice = Label(self.root, text='Invoice No.', font=('goudy old style', 15), bg='white').place(x=50, y=100)
        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=('goudy old style', 15),
                            bg='lightyellow', relief=RIDGE).place(x=160, y=100, width=180, height=28)

        btn_search = Button(self.root, text='Search', font=('goudy old style', 15), bg='maroon', fg='black', bd=2,
                            cursor='hand2', command=self.search).place(x=360, y=100, width=120, height=28)
        btn_clear = Button(self.root, text='Clear', font=('goudy old style', 15), bg='violet', fg='black', bd=2,
                           cursor='hand2', command=self.clear).place(x=490, y=100, width=120, height=28)

        ########## sales frame ##########
        sales_Frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_Frame.place(x=50, y=140, width=200, height=330)

        scrolly = Scrollbar(sales_Frame, orient=VERTICAL)
        self.sales_list = Listbox(sales_Frame, font=('goudy old style', 15), bg='white', yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH, expand=1)
        self.sales_list.bind('<ButtonRelease-1>', self.get_data)

        ########## bill frame ##########
        bill_Frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_Frame.place(x=280, y=140, width=410, height=330)
        lbl_title2 = Label(bill_Frame, text='Customer Bills Area', font=('goudy old style', 25), bg='#92E3A9',
                           fg='black').pack(
            side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_Frame, orient=VERTICAL)
        self.bill_area = Text(bill_Frame, font=('goudy old style', 15), bg='lightyellow', yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)

        ########## image ##########
        self.billPhoto = Image.open('images/Lesson-bro.png')
        self.billPhoto = self.billPhoto.resize((450, 350), Image.ANTIALIAS)
        self.billPhoto = ImageTk.PhotoImage(self.billPhoto)

        lbl_image = Label(self.root, image=self.billPhoto, bd=0)
        lbl_image.place(x=700, y=110)

        self.show()

    #################################################
    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0, END)
        for i in os.listdir('bill'):
            if i.split('.')[-1] == 'txt':
                self.sales_list.insert(END, i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self, ev):
        index_ = self.sales_list.curselection()
        file_name = self.sales_list.get(index_)
        print(file_name)
        self.bill_area.delete('1.0', END)
        fp = open(f'bill/{file_name}', 'r')
        for i in fp:
            self.bill_area.insert(END, i)
        fp.close()

    def search(self):
        if self.var_invoice.get() == '':
            messagebox.showerror('Error', 'Invoice No. should be required', parent=self.root)

        else:
            # print(self.bill_list, self.var_invoice.get())
            if self.var_invoice.get() in self.bill_list:
                fp = open(f'bill/{self.var_invoice.get()}.txt', 'r')
                self.bill_area.delete('1.0', END)
                self.var_invoice.set('')
                for i in fp:
                    self.bill_area.insert(END, i)
                fp.close()

            else:
                messagebox.showerror('Error', 'Invalid Invoice No.', parent=self.root)
                self.var_invoice.set('')

    def clear(self):
        self.show()
        self.bill_area.delete('1.0', END)


if __name__ == '__main__':
    root = Tk()
    obj = salesClass(root)
    root.mainloop()
