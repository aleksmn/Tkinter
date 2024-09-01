import ttkbootstrap as ttk
from tkinter import messagebox, Listbox

import file_connection

# Содержимое статей (названия и текст статей)
articles = file_connection.get_articles()

# print(articles["Персидская кошка"])

# =========================== Функции ==============================

def show_article():
    '''Функция для отображения выбранной статьи'''
    selected_index = listbox.curselection()

    if selected_index:
        title = listbox.get(selected_index)
        article_text = articles[title]

        print(title, article_text)





# ============== Создание графического интерфейса ==================

# Создание окна
root = ttk.Window(themename="superhero")
root.title("Кошко-вики")
root.resizable(0, 0)
root.configure(padx=20, pady=20)


# Создание списка статей (листбокс)
listbox = Listbox(root, width=40, font=('Helvetica', 12))
listbox.grid(column=0, row=0, columnspan=3, sticky="we")

for article in articles:
    listbox.insert('end', article)


# Создание кнопки "Прочитать"
read_button = ttk.Button(root, text="Прочитать")
read_button.grid(column=0, row=1)


# Создание кнопки "Прочитать"
read_button = ttk.Button(root, text="Прочитать", style="info", command=show_article)
read_button.grid(column=0, row=1, sticky="we")

# Создание кнопки "Добавить статью"
add_button = ttk.Button(root, text="Добавить статью", style="success")
add_button.grid(column=1, row=1, sticky="we")

# Удаление
delete_button = ttk.Button(root, text="Удалить статью", style="danger")
delete_button.grid(column=2, row=1, sticky="we")


# Запуск приложения (всегда последняя строка)
root.mainloop()