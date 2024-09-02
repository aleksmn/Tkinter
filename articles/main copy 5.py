import ttkbootstrap as ttk
from tkinter import messagebox, Listbox

import file_connection

# Содержимое статей (названия и текст статей)
articles = file_connection.get_articles()


# =========================== Функции ==============================

def show_article():
    '''Функция для отображения выбранной статьи'''
    selected_index = listbox.curselection()

    if selected_index:
        # название статьи
        title = listbox.get(selected_index)
        # Текст статьи
        article_text = articles[title]
        
        # создаем окно для чтения статьи
        show_window = ttk.Toplevel(root)
        show_window.configure(padx=20, pady=20)
        show_window.resizable(0,0)
        show_window.title(title)

        # Создание виджета Label для отображения названия статьи
        title_label = ttk.Label(show_window, text=title, font=("Helvetica", 14))
        title_label.grid(column=0, row=0)

        # Создание текстового виджета для отображения текста статьи
        textbox = ttk.Text(show_window, wrap='word')
        textbox.grid(column=0, row=1)
        textbox.insert('end', article_text)
        textbox.configure(state="disabled")




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