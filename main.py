import tkinter as tk
from tkinter import ttk

#Kлacc главного окна
class Main(tk.Frame):
    def __init_(self, root):
        super().__init__(root)
        self.init_main()
    
    # Создание и работа с главным окном
    def init_main(self):
        toolbar = tk. Frame(bg=' #d7d7d7',bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # Открытие нового окна по кнопке Добавить
        self.add_img = tk.PhotoImage(file='./img/add-png')
        btn_add = tk.Button(toolbar, bg='#d7d7d7', bd=0, 
                            image=self.add_img, command=self.open_child)
        btn_add. pack (side=tk.LEFT)

        # Добавляем таблицы
        self.tree = ttk.Treeview(self, columns= ('ID', 'name' , 'phone' , 'email'),
                                height=45, show="headings")
        
        # Добавить параметры колонкам
        self.tree.column('ID', width=45, anchor=tk.CENTER)
        self.tree.column('name', width=300, anchor=tk.CENTER)
        self.tree.column ('phone', width=150, anchor=tk.CENTER)
        self.tree.column('email', width=150, anchor=tk.CENTER)

        # Подписи колонок
        self.tree.heading("ID", text="ID")
        self.tree.heading("name", text="ФИ0")
        self.tree.heading("phone", text="Телефон")
        self.tree.heading ("email", text="E-mail")

        #Упаковка
        self.tree.pack(side=tk.LEFT)

    def open_child(self):
        Child()

# Создание дочерних окон
class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    # Создание и работа с дочерним окном
    def init_child(self):
        self.title('Добавить контакт')
        self.geometry('400x200')
        # перехватываем все события происходящие в приложении
        self.grab_set ()
        # захватываем фокус
        self.focus_set()

        label_name = tk.Label (self, text='ФИ0: ')
        label_name. place(x=50, y=50)
        label_phone = tk.Label(self, text= 'Телефон: ')
        label_phone. place(x=50, y=80)
        label_email = tk.Label(self, text='E-mail: ')
        label_email. place(x=50, y=110)

        self.entry_name = ttk. Entry(self)
        self.entry_name.place(x=200, y=50)
        self.entry_phone = ttk.Entry(self)
        self. entry_phone.place(x=200, y=80)
        self.entry_email = ttk.Entry(self)
        self.entry_email. place (x=200, y=110)

        # Кнопка закрытия
        self.btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        self.btn_cancel.place(x=300, y=170)

        # Кнопка добавления
        self.btn_add = ttk.Button(self, text='Добавить')
        self.btn_add.place(x=220, y=170)
        self.btn_add.bind ('‹Button-1>')



# Создание окна
if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('Телефонная книга')
    root.geometry('645x450')
    root.resizable(False,False)
    root.configure('bg= White')
    root.mainloop()