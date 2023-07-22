import tkinter as tk
from tkinter import ttk


class Scrollbar(ttk.Scrollbar):
    def __init__(self, root, tree, **kw):
        super().__init__(root, **kw)
        tree.configure(yscroll=self.set)
        self.grid(row=0, column=2, sticky='ns')
