import ttkbootstrap as ttk
from tkinter import messagebox, Listbox

import file_connection


# Получим все статьи из файла
articles = file_connection.get_articles()




# Создаем окно
root = ttk.Window(themename="superhero")
root.title("Кошко-вики")
root.resizable(0, 0)
root.configure(padx=20, pady=20)

# Создадим список статей
listbox = Listbox(root)
listbox.grid(column=0, row=0, columnspan=3, sticky="we")

# Заполним список статьями
for article in articles:
    listbox.insert("end", article)
    print(article)


# Создание кнопки "Прочитать"
read_button = ttk.Button(root, text="Прочитать")
read_button.grid(column=0, row=1)

# Создание кнопки "Добавить статью"
add_button = 

# Удаление
delete_button = 




# Запуск приложения (последняя строка)
root.mainloop()