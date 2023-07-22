import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from package.product import Product
from package.inputforms import InputForms
from package.viewdata import ViewData
from package.database import Database


class App(tk.Tk):
    def __init__(self, **kw):
        super().__init__()
        self.config(kw)
        self.database = Database.get_instance().connect(kw.get('path_to_db'))
        self.forms = InputForms(self, kw.get('date'))
        self.tree = ViewData(self, columns=(
            'id', 'Название товара', 'Цена', 'Категория'), show="headings")

        # Сохраняем в БД
        self.btn_saved = tk.Button(
            self.master, text="Сохранить", command=self.save_data)
        self.btn_saved.grid(row=8, column=0)

        # Отрисовываем данные в treeview, если они есть в БД
        self.load_data_from_db()

    def close_window(self, event):
        isExit = messagebox.askokcancel(
            'Выйти', 'Вы действительно хотите выйти из приложения?')
        if isExit:
            self.database.destroy()
            self.destroy()

    def config(self, kw):
        self.title(kw.get('title'))  # Устанавливаем заголовок окна
        self.geometry(kw.get('size'))  # Устанавливаем размер окна
        # Зкрытие приложения
        self.protocol("WM_DELETE_WINDOW", lambda e=None: self.close_window(e))
        self.bind('<Escape>', lambda e: self.close_window(e))

        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

    def save_data(self):
        self.database.add_product(self.forms.getItems())
        self.tree.last_id_elem = self.tree.last_id_elem + 1
        product = self.database.get_product(self.tree.last_id_elem)
        self.tree.insert_one_elem(product)
        self.forms.clear()

    def load_data_from_db(self):
        data = self.database.get_all_products()
        if data:
            # last elem id
            last_id_elem = data[-1][0]
            self.tree.last_id_elem = last_id_elem

            self.tree.insert_many_elem(data)
