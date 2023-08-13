import tkinter as tk


def move_task(event, source_list, target_list):

    try:
        # Получение выбранной задачи
        task = source_list.get(source_list.curselection())
        print(task)
        # Перемещение задачи из одной доски в другую
        source_list.delete(source_list.curselection())
        target_list.insert("end", task)
    except Exception as e:
        # print("Ошибка ", e)
        print("Listbox пуст!")

def create_task(event):
    # Добавление новой задачи в список "To Do"
    task = entry.get()
    if task:
        todo_list.insert("end", task)
        entry.delete(0, "end")

# Создание главного окна
root = tk.Tk()
root.title("Kanban Board")

# Создание списков задач
todo_list = tk.Listbox(root, height=10, width=30)
in_progress_list = tk.Listbox(root, height=10, width=30)
done_list = tk.Listbox(root, height=10, width=30)

# Расположение списков на доске
todo_list.grid(row=0, column=0, padx=10, pady=10)
in_progress_list.grid(row=0, column=1, padx=10, pady=10)
done_list.grid(row=0, column=2, padx=10, pady=10)

# Создание виджетов интерфейса
add_label = tk.Label(root, text="Add Task:")
add_label.grid(row=1, column=0, pady=5)

entry = tk.Entry(root, width=30)
entry.grid(row=1, column=1, pady=5)

add_button = tk.Button(root, text="Add", width=10)
add_button.grid(row=1, column=2, pady=5)
add_button.bind("<Button-1>", create_task)

# Привязка событий перемещения задачи между списками
todo_list.bind("<<ListboxSelect>>", lambda e: move_task(e, todo_list, in_progress_list))
in_progress_list.bind("<<ListboxSelect>>", lambda e: move_task(e, in_progress_list, done_list))
done_list.bind("<<ListboxSelect>>", lambda e: move_task(e, done_list, todo_list))

# Запуск главного цикла событий
root.mainloop()
