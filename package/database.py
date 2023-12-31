import sqlite3
import os


class Database:
    _instance = None

    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        if not Database._instance:
            Database._instance = Database()
        return Database._instance

    def connect(self, db_file):
        """ Подключаемся к БД """
        
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_start_table()
        return self

    def create_start_table(self):
        """ Создаем первоначальную таблицу, если она не создана """

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                date TEXT,
                name TEXT,
                price REAL,
                category TEXT
);""")

    def add_product(self, product):
        """ 
        Добавляем продукт в базу данных
        product - это кортеж (date, name, price, category)
        """
        self.cursor.execute("""
            INSERT INTO products (date, name, price, category)
            VALUES (?, ?, ?, ?)
        """, product)

        self.connection.commit()
        print(f'Продукт "{product[1]}" был успешно добавлен в БД')

    def update(self, id, product):
        """ Обновляем продукт по id """

        self.cursor.execute(f"""
            UPDATE products 
            SET date = ? , name= ?, category = ?, price = ?
            WHERE id={id}
        """, product)

        self.connection.commit()
        self.cursor.close()

    def get_all_products(self):
        """ Получаем список всех товаров из БД """

        self.cursor.execute("""SELECT * FROM products""")
        return self.cursor.fetchall()

    def destroy(self):
        """ Закрываем соединение с БД"""
        
        self.cursor.close()

    def get_product(self, id):
        """ Получаем продукт по id """
        
        self.cursor.execute("SELECT * FROM products WHERE id=?", (id,))
        row = self.cursor.fetchone()
        return row


if __name__ == "__main__":
    db = Database.get_instance()
    db.connect(os.path.join(os.getcwd(), 'db', 'products.db'))
    res = db.get_all_products()
    print(res)
    db.destroy()