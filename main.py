import tkinter as tk
import os
from package.app import App

path_to_db = os.path.join(os.getcwd(), 'db', 'products.db')

app = App(path=path_to_db)
app.mainloop()