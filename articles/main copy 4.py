import ttkbootstrap as ttk
from tkinter import messagebox, Listbox

import file_connection

# Получаем все статьи из файла
articles = file_connection.get_articles()

def show_article():
    # Получаем индекс выбранной статьи
    selected_index = listbox.curselection()
    if selected_index:
        title = listbox.get(selected_index)
        article_text = articles[title]
        print(title, article_text)

        # создаем окно для чтения статьи
        show_window = ttk.Toplevel(root)



# Создаем окно
root = ttk.Window(title="Кошко-вики", themename="superhero")

root.resizable(0, 0)
# Отступы
root.configure(padx=20, pady=20)

# Создаем список статей
listbox = Listbox(root, font=(None, 14))

listbox.grid(row=0, column=0, columnspan=3, sticky="we", pady=(0, 10))

# Заполняем виджет листбокс статьями
for artcle in articles:
    listbox.insert("end", artcle)



# Кнопка Прочитать
read_button = ttk.Button(root, text="Прочитать", style="info")
read_button.grid(row=1, column=0, padx=(0, 10))


# Кнопка Добавить
add_button = ttk.Button(root, text="Добавить", style="success")
add_button.grid(row=1, column=1, padx=(0, 10))


# Кнопка Удалить
delete_button = ttk.Button(root, text="Удалить статью", style="danger")
delete_button.grid(column=2, row=1)



# Запуск приложения
root.mainloop()