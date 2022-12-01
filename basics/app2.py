# Buttons and Grid

import tkinter as tk
import os

# Создаем окно программы
root = tk.Tk()
root.title("Работа с кнопками")
root.iconphoto(True, tk.PhotoImage(file='logo.png'))
root.geometry('600x600')
root.resizable(0, 0)
root.config(bg='#10A19D')

# Создаем разметку и кнопки

# Button 1
name_button = tk.Button(root, text='Name')
name_button.grid(row=0, column=0, padx=20, pady=20)

# Button 2
time_button = tk.Button(root, text='Time', bg='lightblue',
                        activebackground='orange')
time_button.grid(row=1, column=1, padx=(0, 20), pady=(0, 20))

# Button 3
date_button = tk.Button(root, text='Date', bg='lightblue',
                        activebackground='orange')
date_button.grid(row=3, column=2, padx=(0, 20), pady=(0, 20), ipadx=30)

# Button 4
place_button = tk.Button(root, text='Place', bg='coral1',
                         activebackground='cornflowerblue',
                         borderwidth=3)
place_button.grid(row=4, column=0,
                  columnspan=3,
                  sticky='we',
                  padx=20, pady=(0, 20), ipadx=20)


# TEST BUTTONS

test_1 = tk.Button(root, text='Test')
test_2 = tk.Button(root, text='Test')
test_3 = tk.Button(root, text='Test')
test_4 = tk.Button(root, text='Test')
test_5 = tk.Button(root, text='Test')
test_6 = tk.Button(root, text='Test')

test_1.grid(row=5, column=0, padx=5, pady=5, sticky='e')
test_2.grid(row=5, column=1, padx=5, pady=5)
test_3.grid(row=5, column=2, padx=5, pady=5, sticky='w')
test_4.grid(row=6, column=0, padx=5, pady=5, sticky='e')
test_5.grid(row=6, column=1, padx=5, pady=5)
test_6.grid(row=6, column=2, padx=5, pady=5, sticky='w')


#  Запускаем основной цикл программы
root.mainloop()
