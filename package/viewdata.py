import tkinter as tk
from tkinter import ttk
import pandas as pd


class ViewData(ttk.Treeview):
    """ data - массив кортежей """

    def __init__(self, root, **kw):
        super().__init__(root, **kw)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 15))

        for named in kw.get('columns'):
            self.heading(named, text=named)

        self.grid(rows=0, column=1)

    def render(self, data):
        for val in data:
            self.insert('', tk.END, values=val)


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
    tree.pack()

    app.mainloop()

    # result = {r: [d[i] for d in data] for i, r in enumerate(columns)}
    # print(result)
