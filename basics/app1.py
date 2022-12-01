import tkinter as tk


# Определяем окно программы
root = tk.Tk()
root.title("Первые виджеты!")
root.iconphoto(True, tk.PhotoImage(file='logo.png'))
root.geometry('600x600')
root.resizable(0, 0)
root.config(bg='#10A19D')

# Создаем виджеты


name_label = tk.Label(root, text='Привет, меня зовут Михаил!')

# Смотрим помощь по этому виджету:
# print(help(name_label))

# Помещаем виджет в окно
name_label.pack()

# Виджет 2

welcome_label = tk.Label(root, text='Добро пожаловать в мое приложение!')
welcome_label.config(font=('Arial', 14, 'bold'), fg='white', bg='#10A19D')

welcome_label.pack(pady=20)


# Виджет 3

text_label = tk.Label(root, text='Это мое первое приложение на Tkinter')
text_label.config(font=('Arial', 12, 'bold'), fg='white', bg='#10A19D')

text_label.pack(pady=(0, 10))


# Виджет 4

text_label = tk.Label(root, text='Здесь я добавил первые виджеты')
text_label.config(font=('Arial', 12, 'bold'), fg='magenta', bg='white')

text_label.pack(pady=(0, 20), ipadx=20, ipady=10, anchor='w')


# Виджет 5

text_label_2 = tk.Label(root, text='и научился добавлять внутренние и внешние отступы')
text_label_2.config(font=('Arial', 12, 'bold'), fg='slateblue', bg='white')
text_label_2.pack(pady=(0, 20), ipadx=20, ipady=10, fill='x')


#  Запускаем основной цикл программы
root.mainloop()
