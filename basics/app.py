import tkinter as tk
import os

print("Рабочая директория", os.getcwd())

# Определяем окно программы
root = tk.Tk()

# Стилизация

root.title("Основы работы с Tkinter!")

# Добавляем логотип на заголовок окна
root.iconphoto(True, tk.PhotoImage(file='logo.png'))

# Другой способ добавления логотипа:
# root.iconbitmap('logo.ico')

root.geometry('650x700')

# root.resizable(0,0)

# Изменяем цвет фона (htps://colorhunt.co)
root.config(bg='#10A19D')


#  Запускаем основной цикл программы
root.mainloop()

