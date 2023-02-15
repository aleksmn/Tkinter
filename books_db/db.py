import sqlite3


class DB:
    def __init__(self):  # конструктор
        # соединяемся с базой данных
        self.conn = sqlite3.connect("mybooks.db")
        self.cur = self.conn.cursor()  # создаем курсор для работы с базой данных
        # SQL запрос для создания таблицы
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, isbn TEXT)")
        self.conn.commit()  # commit - сохраняем изменения

    def __del__(self):  # деструктор
        self.conn.close()  # закрываем связь с базой данных

    def view(self):
        '''Просмотр всей строк в базе данных'''
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def insert(self, title, author, isbn):
        '''Добавление новой записи'''
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?)",
                         (title, author, isbn,))
        self.conn.commit()
        self.view()

    def update(self, id, title, author):
        '''Обновить значения для выбранной строки'''
        self.cur.execute(
            "UPDATE book SET title=?, author=? WHERE id=?", (title, author, id,))
        self.conn.commit()
        self.view()

    def delete(self, id):
        '''Удалить строку по ID'''
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()
        self.view()

    def search(self, title="", author=""):
        '''Поиск по названию или по автору'''
        self.cur.execute(
            "SELECT * FROM book WHERE title=? OR author=?", (title, author,))
        rows = self.cur.fetchall()
        return rows


if __name__ == "__main__":
    db = DB()
    db.insert('Тест Название', "Тест Автор", "Тест ISBN")
    print(db.view())
