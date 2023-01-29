import customtkinter as ctk
from generator import generate_password


number_of_symbols = 14


# Functions
def display_password(number_of_symbols):
    """Выводим пароль на экран"""
    text_output.delete(0, 'end')
    text_output.insert(0, generate_password(number_of_symbols))


root = ctk.CTk()


root.title("Pass Generator")

root.resizable(0, 0)


text_output = ctk.CTkEntry(root,
                           placeholder_text='PASSWORD',
                           corner_radius=0,
                           width=number_of_symbols*14,
                           height=40,
                           justify='center',
                           font=('monospace', 20, 'bold'))


text_output.pack(padx=40, pady=40)

pass_btn = ctk.CTkButton(root,
                         text="Generate",
                         fg_color='slateblue',
                         hover_color='purple',
                         corner_radius=0,
                         font=('sans-serif', 20, 'bold'),
                         width=200,
                         height=40,
                         command=lambda: display_password(number_of_symbols)
                         )
pass_btn.pack(padx=40, pady=(0, 40))

root.mainloop()
