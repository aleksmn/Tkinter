# Матвей

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
        # определяем заголовок статьи
        title = listbox.get(selected_index)
        
        # получаем содержимое статьи из словаря articles
        article_text = articles[title]

        # Создаем новое окно верхнего уровня
        show_window = ttk.Toplevel(root)
        show_window.configure(padx=20, pady=20)
        show_window.resizable(0, 0)
        show_window.title(title)

        # Создание виджета Label для отображения названия статьи
        title_label = ttk.Label(show_window, text=title, font=('Helvetica', 14))
        title_label.grid(row=0, column=0)

        # Создание текстового виджета для отображения текста статьи
        textbox = ttk.Text(show_window, wrap='word')
        textbox.grid(row=1, column=0)

        # Вставляем текст
        textbox.insert('end', article_text)
        # запрещаем редактирование
        textbox.configure(state="disabled")


# Функция для добавления новой статьи
def add_article():
    global articles
    



# Создание окна приложения
# Темные темы: superhero darkly cyborg vapor
# Светлые темы: flatly minty journal pulse morph
root = ttk.Window(themename="cyborg")
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