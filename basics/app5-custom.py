# Radio Buttons

import tkinter as tk
import customtkinter as ctk
from tkinter import IntVar

# Modes: system (default), light, dark
ctk.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
ctk.set_default_color_theme("dark-blue")


# Создаем окно программы
root = ctk.CTk()
root.title("Radio Buttons")
root.iconphoto(True, tk.PhotoImage(file='logo.png'))
root.geometry('350x350')
root.resizable(0, 0)


# Frames

input_frame = ctk.CTkFrame(root,
                           corner_radius=0,
                           width=350,
                           height=50)
output_frame = ctk.CTkFrame(root,
                            corner_radius=0,
                            width=350,
                            height=300)

input_frame.pack(padx=20, pady=20, fill="both", expand=True)
output_frame.pack(padx=20, pady=(0, 20))


# Widgets

number = IntVar()

radio_1 = ctk.CTkRadioButton(input_frame, text='One', variable=number)
radio_2 = ctk.CTkRadioButton(input_frame, text='Two', variable=number)
print_button = ctk.CTkButton(input_frame, text="Print")


radio_1.grid(row=0, column=0, padx=(30, 10), pady=10)
radio_2.grid(row=0, column=1, padx=10, pady=10)
print_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)

# MAINLOOP
root.mainloop()
