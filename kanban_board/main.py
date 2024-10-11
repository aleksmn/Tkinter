import tkinter as tk
import ttkbootstrap as ttk
import json

# Запаковка в исполняемый файл
# pip install auto-py-to-exe
# выполняем команду
# auto-py-to-exe

# Функции

def move_task(event, source_list, target_list=None):

    selected = source_list.curselection()

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


def load_tasks():
    try:
        # получаем списки из json
        with open("tasks.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        # заполняем листбоксы
        # listbox.insert("end", "что вставить")
        for task in data["to_do"]:
            todo_list.insert("end", task)

        for task in data["in_progress"]:
            in_progress_list.insert("end", task)

        for task in data["done"]:  
            done_list.insert("end", task)

    except FileNotFoundError:
        print("Файл с задачами не найден")





def save_tasks():
    tasks = {"to_do": [],
             "in_progress": [],
             "done": []}
    
    # Получаем списки задач
    tasks["to_do"] = todo_list.get(0, "end")
    tasks["in_progress"] = in_progress_list.get(0, "end")
    tasks["done"] = done_list.get(0, "end")



    with open("tasks.json", "w", encoding="utf-8") as json_file:
        json.dump(tasks, json_file, ensure_ascii=False)




def on_closing():

    # Выполняем сохранение списков
    save_tasks()

    # Выход из программы
    root.destroy()



def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")



# Создание главного окна
root = ttk.Window(themename="superhero")

FONT = ("Arial", 10, "bold")

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
todo_list.grid(row=1, column=0, padx=20, pady=(0,20))
in_progress_list.grid(row=1, column=1, padx=(0, 20), pady=(0,20))
done_list.grid(row=1, column=2, padx=(0, 20), pady=(0,20))


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
todo_list.bind("<Double-Button-1>", lambda e: move_task(e, todo_list, in_progress_list))
todo_list.bind("<Right>", lambda e: move_task(e, todo_list, in_progress_list))

in_progress_list.bind("<Double-Button-1>", lambda e: move_task(e, in_progress_list, done_list))
in_progress_list.bind("<Right>", lambda e: move_task(e, in_progress_list, done_list))
in_progress_list.bind("<Left>", lambda e: move_task(e, in_progress_list, todo_list))

done_list.bind("<Double-Button-1>", lambda e: move_task(e, done_list))
done_list.bind("<Right>", lambda e: move_task(e, done_list))
done_list.bind("<Left>", lambda e: move_task(e, done_list, in_progress_list))


# Загружаем задачи из файла
load_tasks()


# Отслеживаем событие закрытие окна
root.protocol("WM_DELETE_WINDOW", on_closing)


center_window(root)

# Запуск главного цикла событий
root.mainloop()