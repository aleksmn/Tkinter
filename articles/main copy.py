import ttkbootstrap as ttk
from tkinter import messagebox, Listbox

import file_connection


# Получим все статьи из файла
articles = file_connection.get_articles()


# Функции
# Функция для отображения выбранной статьи
def show_article():

    selected_index = listbox.curselection()
    if selected_index:
        title = listbox.get(selected_index)
        article_text = articles[title]
        # print(title, article_text)
        # создаем окно для чтения статьи
        show_window = ttk.Toplevel(root)
        show_window.configure(padx=20, pady=20)
        # show_window.geometry("+600+100")
        show_window.title(title)

        # Создание виджета Label для отображения названия статьи
        title_label = ttk.Label(show_window, text=title, font=("Helvetica", 14))
        title_label.grid(column=0, row=0)

        # Создание текстового виджета для отображения текста статьи
        textbox = ttk.Text(show_window, wrap='word')
        textbox.grid(column=0, row=1)

        textbox.delete(1.0, 'end')
        textbox.insert('end', article_text)
        title_label.config(text=title)
        textbox.configure(state="disabled")


# Функция для добавления новой статьи
def add_article():
    global articles

    def save_new_article():
        new_title = entry_title.get()
        new_text = text.get("1.0", 'end')

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



# Функция для удаления статьи
def delete_article():
    global articles, listbox
    selected_index = listbox.curselection()
    if selected_index:
        title = listbox.get(selected_index)
        answer = messagebox.askyesno("Удаление", "Вы действительно хотите удалить эту статью?")
        if answer:
            del articles[title]
            listbox.delete(selected_index)
            file_connection.delete_article(title)


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
read_button = ttk.Button(root, text="Прочитать", style="info")
read_button.grid(column=0, row=1)

# Создание кнопки "Добавить статью"
add_button = ttk.Button(root, text="Добавить статью")
add_button.grid(column=1, row=1)

# Удаление
delete_button = ttk.Button(root, text="Удалить статью", style="danger")
delete_button.grid(column=2, row=1)


# Запуск приложения (последняя строка)
root.mainloop()