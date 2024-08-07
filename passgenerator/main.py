import customtkinter as ctk

from generator import generate_password


# Настройка кол-ва символов в пароле
number_of_symbols = 18


# # # Functions
def display_password(number_of_symbols):

    # Получаем кол-во символов из поля для ввода
    try:
        number_of_symbols = int(text_output.get())
    except:
        pass

    # Выводим пароль на экран
    text_output.delete(0, "end")
    text_output.insert(0, generate_password(number_of_symbols))


# Настройка интерфейса программы

ctk.set_appearance_mode("dark")

root = ctk.CTk()

root.title("Pass Generator")

root.resizable(0, 0)


text_output = ctk.CTkEntry(root,
                           placeholder_text='PASSWORD',
                           corner_radius=0,
                           width=16*number_of_symbols,
                           height=40,
                           justify='center',
                           font=('monospace', 20, 'bold'))

# размещаем виджет по сетке
text_output.grid(column=0, row=0, padx=40, pady=40)


pass_btn = ctk.CTkButton(root,
                         text="Generate",
                         fg_color='purple',
                         hover_color='black',
                         corner_radius=0,
                         font=('sans-serif', 20, 'bold'),
                         height=40,
                         command=lambda: display_password(number_of_symbols))


pass_btn.grid(column=0, row=1, padx=40, pady=(0, 40), sticky="we")



# Последняя строка
root.mainloop()
