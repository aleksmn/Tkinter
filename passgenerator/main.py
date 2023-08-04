import customtkinter as ctk

from generator import generate_password

# Настройка кол-ва символов в пароле
number_of_symbols = 18


# # Functions
def display_password(number_of_symbols):
    """Выводим пароль на экран"""
    text_output.delete(0, 'end')
    text_output.insert(0, generate_password(number_of_symbols))


# Настройка интерфейса программы

ctk.set_appearance_mode("dark")

root = ctk.CTk()

root.title("Pass Generator")

root.resizable(0, 0)

root.configure(fg_color='#2A2F4F')

text_output = ctk.CTkEntry(root,
                           placeholder_text='PASSWORD',
                           corner_radius=0,
                           fg_color='#F0F0F0',
                           text_color='#555',
                           width=14*number_of_symbols,
                           height=40,
                           justify='center',
                           font=('monospace', 20, 'bold'))


text_output.grid(column=0, row=0, padx=40, pady=40)


pass_btn = ctk.CTkButton(root,
                         text="Generate",
                         fg_color='#39B5E0',
                         hover_color='#A31ACB',
                         corner_radius=0,
                         font=('sans-serif', 20, 'bold'),
                         height=40,
                         command=lambda:display_password(number_of_symbols))


pass_btn.grid(column=0, row=1, padx=40, pady=(0, 40), sticky="we")







# Последняя строка
root.mainloop()
