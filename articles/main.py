import ttkbootstrap as ttk
from tkinter import messagebox, Listbox

import file_connection

# Содержимое статей (названия и текст статей)
articles = file_connection.get_articles()


# Создание окна
root = ttk.Window(themename="superhero")
root.title("Кошко-вики")
root.resizable(0, 0)
root.configure(padx=20, pady=20)
root.iconbitmap('icon.ico')

# Создание списка статей
listbox = Listbox(root)
listbox.grid(column=0, row=0, columnspan=3, sticky="we")

# Заполнение списка статьями
for article in articles:
    listbox.insert('end', article)

# Создание кнопки "Прочитать"
read_button = ttk.Button(root, text="Прочитать", style="info")
read_button.grid(column=0, row=1)

# Создание кнопки "Добавить статью"
add_button = ttk.Button(root, text="Добавить статью")
add_button.grid(column=1, row=1)

# Удаление
delete_button = ttk.Button(root, text="Удалить статью", style="danger")
delete_button.grid(column=2, row=1)



# Запуск приложения
root.mainloop()


