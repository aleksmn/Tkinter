# Арсений

import ttkbootstrap as ttk
from tkinter import messagebox, Listbox

import file_connection

# Содержимое статей (названия и текст статей)
articles = file_connection.get_articles()

# Функции



# Создание окна приложения
# Темные темы: superhero darkly cyborg vapor
# Светлые темы: flatly minty journal pulse morph
root = ttk.Window(themename="morph")
root.title("Кошко-вики")
root.resizable(0, 0)
root.configure(padx=20, pady=20)

# Создание списка статей
listbox = Listbox(root)
listbox.grid(column=0, row=0, columnspan=3, sticky="we")

# Заполним список статьями
for article in articles:
    listbox.insert("end", article)

# Добавим кнопки 
# Кнопка Прочитать
read_button = ttk.Button(root, text="Прочитать", style="info")
read_button.grid(column=0, row=1)

# Кнопка Добавить статью
add_button = ttk.Button(root, text="Добавить статью")
add_button.grid(column=1, row=1)

# Кнопка Удалить
delete_button = ttk.Button(root, text="Удалить статью", style="danger")
delete_button.grid(column=2, row=1)



# Запуск программы
root.mainloop()