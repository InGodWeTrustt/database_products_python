import tkinter as tk
import os
from package.app import App
from datetime import date

app_config = {
    "title" : "База данных \"Продукты\"",
    "size" : "1280x720",
    "path_to_db": os.path.join(os.getcwd(), 'db', 'products.db'),
    "date": date.today().strftime('%d.%m.%Y')  # Текущая дата
}

app = App(**app_config)
app.mainloop()
