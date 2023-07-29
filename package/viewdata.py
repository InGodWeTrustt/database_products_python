import tkinter as tk
from tkinter import ttk
import pandas as pd


class ViewData(ttk.Treeview):
    """ data - массив кортежей """

    def __init__(self, root, **kw):
        super().__init__(root, **kw)
        self._last_id_elem = 0
        style = ttk.Style()

        for named in kw.get('columns'):
            self.heading(named, text=named)

        self.grid(row=0, column=1)

    def insert_many_elem(self, data):
        for val in data:
            self.insert('', tk.END, values=val)

    def clear_all(self):
        for item in self.get_children():
            self.delete(item)

    def insert_one_elem(self, data):
        self.insert("", tk.END, values=data)

    @property
    def last_id_elem(self):
        return self._last_id_elem

    @last_id_elem.setter
    def last_id_elem(self, id):
        self._last_id_elem = id

if __name__ == "__main__":
    app = tk.Tk()
    app.geometry('1280x720')
    # columns = ('Название', 'Цена')
    # data = [('Творог', 50), ("Каша", 79)]
    # view = ViewData(app, data, columns=columns, show="headings")
    # view.grid(row=0, column=0)

    tree = ttk.Treeview(app, columns=('id', 'id2'), show="headings")
    tree.heading('id', text="id")
    tree.heading('id2', text="id2")
    tree.insert('', tk.END, values=(1, 4))
    tree.insert('', tk.END, values=(1, 6))
    tree.pack()

    total = 0
    for item in tree.get_children():
        value = tree.item(item, "values")[1]
        total += float(value)
    print(total)

    app.mainloop()

    # result = {r: [d[i] for d in data] for i, r in enumerate(columns)}
    # print(result)
