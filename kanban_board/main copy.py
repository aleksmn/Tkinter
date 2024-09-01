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



# Запуск главного цикла событий
root.mainloop()