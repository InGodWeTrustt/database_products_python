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
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_start_table()
 
    def create_start_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                date TEXT,
                name TEXT,
                price REAL,
                category TEXT
);""")

    def add_product(self, date, name, price, category):
        self.cursor.execute("""
            INSERT INTO products (date, name, price, category)
            VALUES (?, ?, ?, ?)
        """, (date, name, price, category))

        self.connection.commit()
        print(f'Продукт "{name}" был успешно добавлен в БД')

    def update(self, id):
        conn = sqlite3.connect(Product.path_to_db)
        cursor = conn.cursor()

        cursor.execute(f"""
            UPDATE products 
            SET name= ?, category = ?, price = ?
            WHERE id={id}
        """, ((self.name, self.category, self.price)))

        conn.commit()
        conn.close()

    def get_all_products(self):
        self.cursor.execute("""SELECT * FROM products""")
        return self.cursor.fetchall()
    
    def destroy(self):
        self.cursor.close()


if __name__ == "__main__":
    db = Database.get_instance()
    db.connect(os.path.join(os.getcwd(), 'db', 'products.db'))
    # db.add_product('a', 500, 'разное', 2)
    # db.add_product('б', 400, 'другое', 2)
    res = db.get_all_products()
    print(res)
    db.destroy()