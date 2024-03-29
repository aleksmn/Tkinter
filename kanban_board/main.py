import tkinter as tk
import ttkbootstrap as ttk

# Функции

def move_task(event, source_list, target_list=None):

    selected = source_list.curselection()
    print(selected)

    if selected:
        # Получение выбранной задачи
        task = source_list.get(selected)
        # # Перемещение задачи из одной доски в другую
        source_list.delete(selected)
        if target_list:
            target_list.insert("end", task)


def create_task(event):
    # Добавление новой задачи в список "To Do"
    task = entry.get()
    if task:
        todo_list.insert("end", task)
        entry.delete(0, "end")


# Создание главного окна
root = ttk.Window(themename="flatly")

FONT = ("monospace", 10, "bold")

root.title("Kanban Board")
root.resizable(0, 0)


# Подписи для колонок
todo_label = ttk.Label(root, text="To Do", style="warning", font=FONT)
in_progress_label = ttk.Label(root, text="In Progress", style='primary', font=FONT)
done_label = ttk.Label(root, text="Done", style="info", font=FONT)

# Расположение подписей
todo_label.grid(row=0, column=0, pady=(20,0))
in_progress_label.grid(row=0, column=1, pady=(20,0))
done_label.grid(row=0, column=2, pady=(20,0))


# Создание списков задач
todo_list = tk.Listbox(root, height=10, width=30, font=FONT)
in_progress_list = tk.Listbox(root, height=10, width=30, font=FONT)
done_list = tk.Listbox(root, height=10, width=30, font=FONT)


# Расположение списков
todo_list.grid(row=1, column=0, padx=20, pady=20)
in_progress_list.grid(row=1, column=1, padx=(0, 20), pady=20)
done_list.grid(row=1, column=2, padx=(0, 20), pady=20)


# Создание виджетов интерфейса
add_label = ttk.Label(root, text="Add Task:", font=FONT)
add_label.grid(row=2, column=0, pady=(0,20), padx=(0, 20), sticky='e')

entry = ttk.Entry(root, width=30)
entry.grid(row=2, column=1, pady=(0,20), padx=(0, 20), sticky="ew")

add_button = ttk.Button(root, text="Add", width=10)
add_button.grid(row=2, column=2, pady=(0,20), sticky='w')


# События
add_button.bind("<Button-1>", create_task)
entry.bind("<Return>", create_task)


# Привязка событий перемещения задачи между списками
todo_list.bind("<<ListboxSelect>>", lambda e: move_task(e, todo_list, in_progress_list))
in_progress_list.bind("<<ListboxSelect>>", lambda e: move_task(e, in_progress_list, done_list))
done_list.bind("<<ListboxSelect>>", lambda e: move_task(e, done_list))

# Запуск главного цикла событий
root.mainloop()
