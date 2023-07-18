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
        self.tree = ViewData(self, columns=('id', 'Название товара', 'Цена', 'Категория'))

    def close_window(self, event):
        isExit = messagebox.askokcancel(
            'Выйти', 'Вы действительно хотите выйти из приложения?')
        if isExit:
            self.destroy()

    def config(self):
        self.title('База данных "Продукты"')  # Устанавливаем заголовок окна
        self.geometry('1280x720')  # Устанавливаем размер окна
        self.date = date.today().strftime('%d.%m.%Y')  # Текущая дата
        # Зкрытие приложения
        self.protocol("WM_DELETE_WINDOW", lambda e=None: self.close_window(e))
        self.bind('<Escape>', lambda e: self.close_window(e))
