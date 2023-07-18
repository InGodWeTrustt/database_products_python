import tkinter as tk
import datetime
from package.opt_menu import OptMenu as OptionMenu
from package.product import Product


class InputForms:
    def __init__(self, root, cur_date):
        self.master = root
        self.date = cur_date
        self.__create_fields()

    def __create_fields(self):
        tk.Label(self.master, text="Дата").grid(row=0, column=0)
        self.date_label = tk.Label(self.master, text=self.date)
        self.date_label.grid(row=1, column=0)

        tk.Label(self.master, text="Наименование товара").grid(row=2, column=0)
        self.product_name = tk.Entry(self.master)
        self.product_name.grid(row=3, column=0)

        tk.Label(self.master, text="Цена").grid(row=4, column=0)
        self.price = tk.Entry(self.master)
        self.price.grid(row=5, column=0)

        # Создаем выпадающее меню для категории
        tk.Label(self.master, text="Категория").grid(row=6, column=0)
        opt_menu = OptionMenu(self.master, row_idx=7, col_idx=0)
        self.category = opt_menu.category_value

        # Сохраняем в БД
        self.btn_saved = tk.Button(
            self.master, text="Сохранить", command=self.save_data)
        self.btn_saved.grid(row=8, column=0)

    def clear(self):
        self.product_name.delete("0", tk.END)
        self.price.delete("0", tk.END)

    
    def save_data(self):
        name = self.product_name.get()
        price = float(self.price.get().replace(',', '.'))
        category = self.category

        Product(self.date, name, category, price).save()

    # def update_data(self):
    #     name = self.product_name.get()
    #     price = float(self.price.get().replace(',', '.'))
    #     quantity = float(self.quantity.get())

    #     Product(self.date, name, category, price).update()
