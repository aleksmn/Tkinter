# Арсений

import ttkbootstrap as ttk
from tkinter import messagebox, Listbox

import file_connection

# Содержимое статей (названия и текст статей)
articles = file_connection.get_articles()

# Функции
# Функция для отображения выбранной статьи
def show_article():
    selected_index = listbox.curselection()
    if selected_index:
        title = listbox.get(selected_index)
        article_text = articles[title]

        print(title, article_text)
        # Создаем окно верхенго уровня
        show_window = ttk.Toplevel(root)
        show_window.title(title)
        show_window.resizable(0, 0)
        show_window.configure(padx=20, pady=20)

        # Создание виджета Label для отображения названия статьи
        title_label = ttk.Label(show_window, text=title, font=("Helvetica", 14))
        title_label.grid(column=0, row=0)
     
        # Создание текстового виджета для отображения текста статьи
        textbox = ttk.Text(show_window, wrap='word')
        textbox.grid(column=0, row=1)
        # Добавляем текст в виджет
        textbox.insert('end', article_text)
        textbox.configure(state="disabled")


def add_article():
    
    add_window = ttk.Toplevel(root)
    add_window.title("Добавить статью")
    add_window.configure(padx=20, pady=20)

    label_title = ttk.Label(add_window, text="Введите название статьи:")
    label_title.grid()
    # Поле для ввода названия
    entry_title = ttk.Entry(add_window)
    entry_title.grid(sticky="we")

    label_text = ttk.Label(add_window, text="Введите текст статьи:")
    label_text.grid()
    text = ttk.Text(add_window, wrap='word')
    text.grid()

    # Кнопка для сохранения
    save_button = 




# Создание окна приложения
# Темные темы: superhero darkly cyborg vapor
# Светлые темы: flatly minty journal pulse morph
root = ttk.Window(themename="pulse")
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
read_button = ttk.Button(root, text="Прочитать", style="info", command=show_article)
read_button.grid(column=0, row=1)

# Кнопка Добавить статью
add_button = ttk.Button(root, text="Добавить статью")
add_button.grid(column=1, row=1)

# Кнопка Удалить
delete_button = ttk.Button(root, text="Удалить статью", style="danger")
delete_button.grid(column=2, row=1)



# Запуск программы
root.mainloop()