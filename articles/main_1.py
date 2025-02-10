import ttkbootstrap as ttk
from tkinter import messagebox, Listbox

import file_connection

# Содержимое статей (названия и текст статей)
articles = file_connection.get_articles()

# Функция для отображения выбранной статьи
def show_article():
    selected_index = listbox.curselection()
    if selected_index:
        title = listbox.get(selected_index)
        article_text = articles[title]
        
        # создаем окно для чтения статьи
        show_window = ttk.Toplevel(root)
        show_window.configure(padx=20, pady=20)
        show_window.resizable(0, 0)
        show_window.title(title)

        # Создание виджета Label для отображения названия статьи
        title_label = ttk.Label(show_window, text=title, font=("Helvetica", 14))
        title_label.grid(column=0, row=0)

        # Создание текстового виджета для отображения текста статьи
        textbox = ttk.Text(show_window, wrap='word')
        textbox.grid(column=0, row=1)
        textbox.insert('end', article_text)
        textbox.configure(state="disabled")



# Создание окна
root = ttk.Window(themename="superhero")
root.title("Кошко-вики")
root.resizable(0, 0)
root.configure(padx=20, pady=20)
# root.iconbitmap('icon.ico')

# Создание списка статей
listbox = Listbox(root)
listbox.grid(column=0, row=0, columnspan=3, sticky="we")

# Заполнение списка статьями
for article in articles:
    listbox.insert('end', article)

# Создание кнопки "Прочитать"
read_button = ttk.Button(root, text="Прочитать", style="info", command=show_article)
read_button.grid(column=0, row=1)

# Создание кнопки "Добавить статью"
add_button = ttk.Button(root, text="Добавить статью")
add_button.grid(column=1, row=1)

# Удаление
delete_button = ttk.Button(root, text="Удалить статью", style="danger")
delete_button.grid(column=2, row=1)



# Запуск приложения
root.mainloop()


