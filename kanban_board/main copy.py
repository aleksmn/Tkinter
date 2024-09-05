import tkinter as tk
import ttkbootstrap as ttk






# Создание главного окна
root = ttk.Window(themename="superhero")

root.title("Kanban Board")
root.resizable(0, 0)

# шрифт
FONT = ("monospace", 10, "bold")

# Подписи колонок
todo_label = ttk.Label(root, text="To Do")
in_progress_label = ttk.Label(root, text="In Progress")
done_label = ttk.Label(root, text="Done")


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






# Запуск главного цикла событий
root.mainloop()