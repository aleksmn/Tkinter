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

# Функция для добавления новой статьи
def add_article():
    global articles

    def save_new_article():
        # получим название и текст статьи
        new_title = entry_title.get()
        new_text = text.get("1.0", "end")
        # print(new_title, new_text)
        if new_title and new_text:
            articles[new_title] = new_text
            listbox.insert("end", new_title)
            file_connection.save_article(new_title, new_text)
            add_window.destroy()

    add_window = ttk.Toplevel(root)
    add_window.title("Добавить статью")
    add_window.configure(padx=20, pady=20)

    label_title = ttk.Label(add_window, text="Введите название статьи:")
    label_title.grid()
    entry_title = ttk.Entry(add_window)
    entry_title.grid(sticky="we")

    label_text = ttk.Label(add_window, text="Введите текст статьи:")
    label_text.grid()
    text = ttk.Text(add_window, wrap='word')
    text.grid()

    save_button = ttk.Button(add_window, text="Сохранить", command=save_new_article)
    save_button.grid()



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
add_button = ttk.Button(root, text="Добавить статью", command=add_article)
add_button.grid(column=1, row=1)

# Удаление
delete_button = ttk.Button(root, text="Удалить статью", style="danger")
delete_button.grid(column=2, row=1)



# Запуск приложения
root.mainloop()


