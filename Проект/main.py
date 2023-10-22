import tkinter as tk
#Knacc главного окна
class Main(tk.Frame):
    def __init_(self, root):
        super().__init__(root)
        self.init_main()
    
    # Создание и работа с главным окном
    def init_main(self):
        toolbar = tk. Frame(bg=' #d7d7d7',bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

    def open_child(self):
        Child()

# Создание дочерних окон
class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    # Создание и работа с дочерним окном
    def init_child(self):
        self.title('Добавить')
        self.geometry('400x200')
        # перехватываем все события происходящие в приложении
        self.grab_set ()
        # захватываем фокус
        self.focus_set()