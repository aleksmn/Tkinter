import sqlite3


class DB:  # creating a class DB with functions to perform various operations on the database.
    def __init__(self):  # constructor functor for class DB.
        # connects to a database called mybooks.db
        self.conn = sqlite3.connect("mybooks.db")
        self.cur = self.conn.cursor()  # creating a cursor to navigate through the database
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, isbn TEXT)")  # creating a table called book with id, title, author and isbn as columns.
        self.conn.commit()  # commit functions saves everything to the database

    def __del__(self):  # destructor created for the class DB
        self.conn.close()  # closes the connection with the database

    def view(self):  # To view all the rows present in the table
        # Execute function is to perform the SQL operations. Here, it produces all the rows from the table.
        self.cur.execute("SELECT * FROM book")
        # fetching all the rows one by one from the table and storing it in list rows
        rows = self.cur.fetchall()
        return rows

    def insert(self, title, author, isbn):  # inserting a new row in the table.
        # passing values to the function to store them in the columns
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?)",
                         (title, author, isbn,))
        self.conn.commit()
        self.view()

    # to update the values of the selected row with the values passed by the user
    def update(self, id, title, author):
        self.cur.execute(
            "UPDATE book SET title=?, author=? WHERE id=?", (title, author, id,))
        self.conn.commit()
        self.view()

    # to delete the row from the table given the value of the id of the selected row.
    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()
        self.view()

    # to search for a given entry in the table given either the value of the title or author name
    def search(self, title="", author=""):
        self.cur.execute(
            "SELECT * FROM book WHERE title=? OR author=?", (title, author,))
        rows = self.cur.fetchall()
        return rows



if __name__ == "__main__":
    db = DB()
    db.insert('Тест Название', "Тест Автор", "Тест ISBN")
    print(db.view())