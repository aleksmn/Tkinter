# Frames

import tkinter as tk
import os

# Создаем окно программы
root = tk.Tk()
root.title("Работа с кнопками")
root.iconphoto(True, tk.PhotoImage(file='logo.png'))
root.geometry('600x600')
root.resizable(0, 0)
root.config(bg='azure2')


# Пример, зачем нужны фреймы

# name_label = tk.Label(root, text='Enter your name')
# name_label.pack()
# name_button = tk.Button(root, text='Submit your name')
# name_button.grid(row=0, column=1)


# Создаем фреймы

pack_frame = tk.Frame(root, bg='cyan1')
grid_frame_1 = tk.Frame(root, bg='darkolivegreen1')
grid_frame_2 = tk.LabelFrame(
    root, text="This is Grid Frame!", bg=root['bg'], borderwidth=3)

pack_frame.pack(fill='both', expand=True)
grid_frame_1.pack(fill='both', expand=True)
grid_frame_2.pack(fill='both', expand=True, padx=10, pady=10)

# Pack Frame

pack_frame.config(padx=10, pady=10)

tk.Label(pack_frame, text="Hello World!").pack()
tk.Label(pack_frame, text="Hello World!").pack()
tk.Label(pack_frame, text="Hello World!").pack()


# Grid Frame

grid_frame_1.config(padx=10, pady=10)

tk.Label(grid_frame_1,
         text="Hello World!",
         bg=grid_frame_1['bg'],
         pady=10).grid(row=0, column=0)
tk.Label(grid_frame_1,
         text="Hello World!",
         bg=grid_frame_1['bg'],
         pady=10).grid(row=1, column=1)
tk.Label(grid_frame_1,
         text="Hello World!",
         bg=grid_frame_1['bg'],
         pady=10).grid(row=2, column=2)




# Запускаем основной цикл программы
root.mainloop()
