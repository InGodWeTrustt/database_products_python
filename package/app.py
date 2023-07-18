import tkinter as tk
from tkinter import ttk
from datetime import date
from tkinter import messagebox
from package.product import Product
from package.inputforms import InputForms
from package.viewdata import ViewData
from package.database import Database


class App(tk.Tk):
    def __init__(self, path):
        super().__init__()
        self.config()
        self.database = Database.get_instance().connect(path)
        self.forms = InputForms(self, self.date)
        self.tree = ViewData(self, columns=(
            'id', 'Название товара', 'Цена', 'Категория'))

        # Сохраняем в БД
        self.btn_saved = tk.Button(
            self.master, text="Сохранить", command=self.save_data)
        self.btn_saved.grid(row=8, column=0)

    def close_window(self, event):
        isExit = messagebox.askokcancel(
            'Выйти', 'Вы действительно хотите выйти из приложения?')
        if isExit:
            self.database.destroy()
            self.destroy()

    def config(self):
        self.title('База данных "Продукты"')  # Устанавливаем заголовок окна
        self.geometry('1280x720')  # Устанавливаем размер окна
        self.date = date.today().strftime('%d.%m.%Y')  # Текущая дата
        # Зкрытие приложения
        self.protocol("WM_DELETE_WINDOW", lambda e=None: self.close_window(e))
        self.bind('<Escape>', lambda e: self.close_window(e))

    def save_data(self):
        self.database.add_product(self.forms.getItems())
        products = self.database.get_all_products()
        self.tree.render(products)
        self.forms.clear()
