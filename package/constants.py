import os
from datetime import date

APP_CONFIG = {
    "title" : "База данных \"Продукты\"",
    "size" : "1280x720",
    "path_to_db": os.path.join(os.getcwd(), 'db', 'products.db'),
    "date": date.today().strftime('%d.%m.%Y')  # Текущая дата
}