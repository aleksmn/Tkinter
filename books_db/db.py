import sqlite3


class DB:
    def __init__(self):  # конструктор
        # соединяемся с базой данных
        self.conn = sqlite3.connect("mybooks.db")
        self.cur = self.conn.cursor()  # создаем курсор для работы с базой данных
        # SQL запрос для создания таблицы
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year TEXT)")
        self.conn.commit()  # commit - сохраняем изменения

    def __del__(self):  # деструктор
        self.conn.close()  # закрываем связь с базой данных

    def view(self):
        '''Просмотр всей строк в базе данных'''
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def insert(self, title, author, year):
        '''Добавление новой записи'''
        # SQL запрос
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?)",
                         (title, author, year,))
        self.conn.commit()
        self.view()

    def update(self, id, title, author):
        '''Обновить значения для выбранной строки'''
        # SQL запрос (специальный язык для выполнения действий с базой данных)
        self.cur.execute(
            "UPDATE book SET title=?, author=? WHERE id=?", (title, author, id,))
        self.conn.commit()
        self.view()

    def delete(self, id):
        '''Удалить строку по ID'''
         # SQL запрос 
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
    db.insert('Таинственный остров', 'Верн Ж.', '1998')
    db.insert('Архив Буресвета', 'Сандерсон Б.', '2022')
    db.insert('Властелин колец', 'Толкин Дж.Р.Р.', '2005')
    db.insert('Евгений Онегин', 'Пушкин А. С.', '2001')

    # Изменяем запись с id 1
    db.update('1', '20 тысяч лье под водой', 'Верн Ж.')

    # print(db.view())

    print("Результат поиска: ")
    print(db.search(author='Пушкин А. С.'))
