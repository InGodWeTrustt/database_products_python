import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from package.product import Product
from package.inputforms import InputForms
from package.viewdata import ViewData
from package.database import Database
from package.scrollbar import Scrollbar


class App(tk.Tk):
    def __init__(self, **kw):
        super().__init__()
        self.config(kw)
        self.database = Database.get_instance().connect(kw.get('path_to_db'))
        self.forms = InputForms(self, kw.get('date'))
        self.tree = ViewData(self, columns=(
            'id', "Дата",  'Название товара', 'Цена', 'Категория'), show="headings")
        self.scrollbar = Scrollbar(
            self, self.tree, orient=tk.VERTICAL, command=self.tree.yview)

        # Сохраняем товар в БД
        self.btn_saved = tk.Button(
            self.master, text="Сохранить", command=self.save_data)
        self.btn_saved.grid(row=8, column=0)

        # Отрисовываем данные в treeview, если они есть в БД
        self.load_data_from_db()

        # обработка события при наведении / потери фокуса на кнопку "Сохранить"
        self.enter_leave_events()

        #  Отображение итоговой суммы
        self._finally_price = 0
        self.finally_price_lbl = tk.Label(self, text=f"Итоговая сумма: {str(self.finally_price)} р.", font=(
            "Arial", 20))
        self.finally_price_lbl.grid(column=1, row=2)

        # Обновление итоговой суммы
        self.update_text_finally_price()

    @property
    def finally_price(self):
        return self._finally_price

    @finally_price.setter
    def finally_price(self, new_value):
        self._finally_price = new_value

    def close_window(self, event):
        """Закрытие основного окна приложения"""

        isExit = messagebox.askokcancel(
            'Выйти', 'Вы действительно хотите выйти из приложения?')
        if isExit:
            self.database.destroy()
            self.destroy()

    def config(self, kw):
        """ Начальная конфигурация """

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
        # получаем продукт из базы данных
        product = self.database.get_product(self.tree.last_id_elem)
        # отображаем продукт в treeview
        self.tree.insert_one_elem(product)
        # очищаем поля ввода данных
        self.forms.clear()
        # обновляем итоговую стоимость всех товаров
        self.update_text_finally_price()

    def load_data_from_db(self):
        """ Предварительная загрузка данных из БД прм старте приложения """

        data = self.database.get_all_products()
        if data:
            # last elem id
            last_id_elem = data[-1][0]
            self.tree.last_id_elem = last_id_elem
            self.tree.insert_many_elem(data)

    def enter_leave_events(self):
        """ События на кнопке """

        self.btn_saved.bind('<Enter>', self.on_enter)
        self.btn_saved.bind('<Leave>', self.on_leave)

    def on_enter(self, event):
        """ Функция вызывается, когда курсор мыши наводится на виджет"""

        event.widget.config(bg="blue", fg="white")

    def on_leave(self, event):
        event.widget.config(bg='SystemButtonFace', fg='black')

    def calc_finally_price(self):
        """ Расчет итоговой стоимости всех товаров в БД"""

        total_sum = 0
        for item in self.tree.get_children():
            value = self.tree.item(item)['values'][3]
            total_sum += float(value)
        return total_sum

    def update_text_finally_price(self):
        """ Обновляем итоговую цену в метке"""
        
        self._finally_price = self.calc_finally_price()
        self.finally_price_lbl.config(
            text=f"Итоговая сумма: {str(self.finally_price)} р.")