import sqlite3
import tkinter as tk
import os


class Product:
    def __init__(self, date, name, category, price):
        self.date = date
        self.name = name
        self.category = category
        self.price = price

    def to_tuple(self):
        res = []
        items = ['date', 'name', 'price', 'category']
        for attr in items:
            res.append(getattr(self, attr))
        return tuple(res)

    # def show_all(self, root):
    #     cursor.execute(
    #         f"""SELECT SUM(total_price) FROM products WHERE date={self.date}""")
    #     finally_price = cursor.fetchone()[0]


if __name__ == "__main__":
    # Product(2,'2023','тecn', 4, 200).save_product()
    # Product(2,'2023','тecn', 4, 200).save_product()
    # conn = sqlite3.connect('products.db')
    # cursor = conn.cursor()
    # cursor.execute(""" SELECT * from products""")
    # res = cursor.fetchall()
    # print(Product('2023', 'test', 'cat', 400).to_tuple()) # ('2023', 'test', 'cat', 400)
    pass
