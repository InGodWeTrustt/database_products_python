import sqlite3
import tkinter as tk
from package.viewdata import ViewData
import os


class Product:
    def __init__(self, date, name, category, price):
        self.date = date
        self.name = name
        self.category = category
        self.price = price

    def show_all(self, root):
        conn = sqlite3.connect(Product.path_to_db)
        cursor = conn.cursor()
        cursor.execute(
            """SELECT id, date, name, price, category FROM products""")
        data = cursor.fetchall()

        row = ('Дата', "Наименование товара", "Цена", "Категория")

        if len(data):
            view = ViewData(root, data, columns=row, show="headings")
            view.grid(column=1, rowspan=8)

            cursor.execute(
                f"""SELECT SUM(total_price) FROM products WHERE date={self.date}""")
            finally_price = cursor.fetchone()[0]
            tk.Label(root, text=f"Итоговая сумма: {str(finally_price)} р.", font=(
                "Arial", 25)).grid(column=1, row=7)

        conn.close()


if __name__ == "__main__":
    # Product(2,'2023','тecn', 4, 200).save_product()
    # Product(2,'2023','тecn', 4, 200).save_product()
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute(""" SELECT * from products""")
    res = cursor.fetchall()
