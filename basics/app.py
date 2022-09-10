import tkinter as tk
import os

print("Рабочая директория", os.getcwd())

# Определяем окно программы
root = tk.Tk()

# Стилизация

root.title("Основы работы с Tkinter!")

# Добавляем логотип на заголовок окна
root.iconphoto(True, tk.PhotoImage(file='logo.png'))

root.geometry('650x700')
root.resizable()


#  Запускаем основной цикл программы
root.mainloop()

