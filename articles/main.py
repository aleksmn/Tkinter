import tkinter as tk
import file_connection
from tkinter import messagebox

# Содержимое статей (названия и текст статей)
articles = file_connection.get_articles()

current_article = None

# Функция для отображения выбранной статьи
def show_article():
    global current_article
    selected_index = listbox.curselection()
    if selected_index:
        title = listbox.get(selected_index)
        current_article = title

        # Очистка окна и добавление текста статьи
        text.delete(1.0, tk.END)
        text.insert(tk.END, articles[title])

        # Очистка окна и добавление названия и текста статьи
        title_label.config(text=title)
        title_label.grid()
        text.grid()
        back_button.grid()
        listbox.grid_forget()
        delete_button.grid_forget()
        read_button.grid_forget()
        add_button.grid_forget()


# Функция для возврата к списку статей
def go_back():
    global current_article
    current_article = None

    # Очистка текста статьи и названия, отображение списка статей
    text.delete(1.0, tk.END)
    title_label.config(text="")
    listbox.grid()
    text.grid_forget()
    title_label.grid_forget()
    back_button.grid_forget()
    read_button.grid()
    add_button.grid()
    delete_button.grid()


# Функция для удаления статьи
def delete_article():
    global current_article, articles, listbox
    selected_index = listbox.curselection()
    if selected_index:
        title = listbox.get(selected_index)
        current_article = title
        answer = messagebox.askyesno("Удаление", "Вы действительно хотите удалить эту статью?")
        if answer:
            go_back()
            del articles[title]
            listbox.delete(selected_index)
            file_connection.delete_article(title)


# Функция для добавления новой статьи
def add_article():
    global articles

    def save_new_article():
        new_title = entry_title.get()
        new_text = text.get("1.0", tk.END)
        if new_title and new_text:
            articles[new_title] = new_text
            listbox.insert(0, new_title)
            file_connection.save_article(new_title, new_text)
            add_window.destroy()
            show_article()

    add_window = tk.Toplevel(root)
    add_window.title("Добавить статью")

    label_title = tk.Label(add_window, text="Введите название статьи:")
    label_title.grid()
    entry_title = tk.Entry(add_window)
    entry_title.grid()

    label_text = tk.Label(add_window, text="Введите текст статьи:")
    label_text.grid()
    text = tk.Text(add_window, wrap=tk.WORD)
    text.grid()

    save_button = tk.Button(add_window, text="Сохранить", command=save_new_article)
    save_button.grid()


# Создание окна
root = tk.Tk()
root.title("Кошко-вики")
# root.geometry("600x500")  # Фиксированный размер окна
root.resizable(0, 0)

# Создание списка статей
listbox = tk.Listbox(root)
listbox.grid(column=0, row=0, columnspan=3, sticky="we")

# Заполнение списка статьями
for article in articles:
    listbox.insert(tk.END, article)

# Создание текстового виджета для отображения текста статьи (изначально скрыт)
text = tk.Text(root, wrap=tk.WORD)
text.grid(column=0, row=1)
text.grid_forget()

# Создание виджета Label для отображения названия статьи (изначально скрыт)
title_label = tk.Label(root, text="", font=("Helvetica", 14))
title_label.grid(column=0, row=0)
title_label.grid_forget()

# Создание кнопки "Назад" (изначально скрытой)
back_button = tk.Button(root, text="Назад", command=go_back)
back_button.grid(column=1, row=1)
back_button.grid_forget()

# Создание кнопки "Прочитать"
read_button = tk.Button(root, text="Прочитать", command=show_article)
read_button.grid(column=0, row=1)

# Создание кнопки "Добавить статью"
add_button = tk.Button(root, text="Добавить статью", command=add_article)
add_button.grid(column=1, row=1)

delete_button = tk.Button(root, text="Удалить статью", command=delete_article)
delete_button.grid(column=2, row=1)

# Запуск приложения
root.mainloop()