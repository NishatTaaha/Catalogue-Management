from tkinter import *
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass


class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x700+0+0')
        self.root.title('Inventory Management System')
        self.root.config(bg='white')

        ######### title ##########

        self.icon_title = PhotoImage(file='images/team.png')
        title = Label(self.root, text='Inventory Management App', font=('times new roman', 15, 'bold'), bg='darkblue',
                      fg='white', image=self.icon_title, compound=LEFT, padx=20).place(x=0, y=0, relwidth=1, height=70)

        ############ btn logout ##########
        btn_logout = Button(self.root, text='Logout', font=('times new roman', 15, 'bold'), bg='maroon')

        ############# clock ##############
        self.lbl_clock = Label(self.root, text='Welcome to Inventory management System!!')
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        ######## left menu ############
        self.menuLogo = Image.open('images/community.png')
        self.menuLogo = self.menuLogo.resize((200, 200), Image.ANTIALIAS)
        self.menuLogo = ImageTk.PhotoImage(self.menuLogo)

        leftMenu = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        leftMenu.place(x=0, y=102, width=200, height=565)
        label_menu_logo = Label(leftMenu, image=self.menuLogo)
        label_menu_logo.pack(side=TOP, fill=X)

        self.icon_side = Image.open('images/fast-forward.png')
        self.icon_side = self.icon_side.resize((40, 40), Image.ANTIALIAS)
        self.icon_side = ImageTk.PhotoImage(self.icon_side)
        Label_menu = Label(leftMenu, text='Menu', font=('times new roman', 20), bg='#009688').pack(side=TOP, fill=X)

        btn_employee = Button(leftMenu, image=self.icon_side, text='Employee', compound=LEFT, padx=12, anchor='w',
                              activebackground='darkgray', font=('times new roman', 20, 'bold'), bg='black', fg='white',
                              bd=3, cursor='hand2', command=self.employee).pack(side=TOP, fill=X)
        btn_supplier = Button(leftMenu, image=self.icon_side, text='Supplier', compound=LEFT, padx=12, anchor='w',
                              activebackground='darkgray', font=('times new roman', 20, 'bold'), bg='black', fg='white',
                              bd=3, cursor='hand2', command=self.supplier).pack(side=TOP, fill=X)
        btn_category = Button(leftMenu, image=self.icon_side, text='Category', compound=LEFT, padx=12, anchor='w',
                              activebackground='darkgray', font=('times new roman', 20, 'bold'), bg='black', fg='white',
                              bd=3, cursor='hand2', command=self.category).pack(side=TOP, fill=X)
        btn_product = Button(leftMenu, image=self.icon_side, text='Product', compound=LEFT, padx=12, anchor='w',
                             activebackground='darkgray', font=('times new roman', 20, 'bold'), bg='black', fg='white',
                             bd=3, cursor='hand2', command=self.product).pack(side=TOP, fill=X)
        btn_sales = Button(leftMenu, image=self.icon_side, text='Sales', compound=LEFT, padx=12, anchor='w',
                           activebackground='darkgray', font=('times new roman', 20, 'bold'), bg='black', fg='white',
                           bd=3, cursor='hand2', command=self.sales).pack(side=TOP, fill=X)
        btn_exit = Button(leftMenu, image=self.icon_side, text='Exit', compound=LEFT, padx=12, anchor='w',
                          activebackground='darkgray', font=('times new roman', 20, 'bold'), bg='black', fg='white',
                          bd=3, cursor='hand2').pack(side=TOP, fill=X)

        ########### content ############
        self.label_employee = Label(self.root, text='Total Employee\n[0]', bd=5, bg='pink', fg='white', relief=RIDGE,
                                    font=('goudy old style', 20, 'bold'))
        self.label_employee.place(x=300, y=120, height=150, width=300)

        self.label_Supplier = Label(self.root, text='Total Supplier\n[0]', bd=5, bg='violet', fg='white', relief=RIDGE,
                                    font=('goudy old style', 20, 'bold'))
        self.label_Supplier.place(x=650, y=120, height=150, width=300)

        self.label_Category = Label(self.root, text='Total Category\n[0]', bd=5, bg='darkblue', fg='white',
                                    relief=RIDGE, font=('goudy old style', 20, 'bold'))
        self.label_Category.place(x=1000, y=120, height=150, width=300)

        self.label_Product = Label(self.root, text='Total Product\n[0]', bd=5, bg='maroon', fg='white', relief=RIDGE,
                                   font=('goudy old style', 20, 'bold'))
        self.label_Product.place(x=300, y=300, height=150, width=300)

        self.label_Sales = Label(self.root, text='Total Sales\n[0]', bd=5, bg='purple', fg='white', relief=RIDGE,
                                 font=('goudy old style', 20, 'bold'))
        self.label_Sales.place(x=650, y=300, height=150, width=300)

        ########### footer ############
        lbl_footer = Label(self.root,
                           text='IMS-Inventory Management System\n For any technical issue, Contact: 0155xxxxxxx',
                           font=('times new roman', 12), bg='#4d636d', fg='white').pack(side=BOTTOM, fill=X)

        ##########################################################

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)


if __name__ == '__main__':
    root = Tk()
    obj = IMS(root)
    root.mainloop()
