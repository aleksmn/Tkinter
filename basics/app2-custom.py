# Buttons and Grid

import tkinter as tk
import customtkinter as ctk

# Install
# pip install customtkinter


# Modes: system (default), light, dark
ctk.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
ctk.set_default_color_theme("blue")


# Создаем окно программы
root = ctk.CTk()
root.title("Работа с кнопками")
root.iconphoto(True, tk.PhotoImage(file='logo.png'))
root.geometry('600x600')
root.resizable(0, 0)
# root.config(bg='#10A19D')

# Функции


def button_function():
    print("button pressed")


# Создаем разметку и кнопки

# # Button 1
name_button = ctk.CTkButton(root, text='Name', command=button_function)
name_button.grid(row=0, column=0, padx=20, pady=20)

# # Button 2
time_button = ctk.CTkButton(root, text='Time')
time_button.grid(row=1, column=1, padx=(0, 20), pady=(0, 20))

# # Button 3
date_button = ctk.CTkButton(root, text='Date')
date_button.grid(row=3, column=2, padx=(0, 20), pady=(0, 20), ipadx=30)


# Button 4
place_button = ctk.CTkButton(root, text='Place')
place_button.grid(row=4, column=0, columnspan=3,sticky='we',
                  padx=20, pady=(0, 20), ipadx=20)


# TEST BUTTONS

test_1 = ctk.CTkButton(root, text='Test')
test_2 = ctk.CTkButton(root, text='Test')
test_3 = ctk.CTkButton(root, text='Test')
test_4 = ctk.CTkButton(root, text='Test')
test_5 = ctk.CTkButton(root, text='Test')
test_6 = ctk.CTkButton(root, text='Test')

test_1.grid(row=5, column=0, padx=5, pady=5, sticky='e')
test_2.grid(row=5, column=1, padx=5, pady=5)
test_3.grid(row=5, column=2, padx=5, pady=5, sticky='w')
test_4.grid(row=6, column=0, padx=5, pady=5, sticky='e')
test_5.grid(row=6, column=1, padx=5, pady=5)
test_6.grid(row=6, column=2, padx=5, pady=5, sticky='w')






#  Запускаем основной цикл программы
root.mainloop()
