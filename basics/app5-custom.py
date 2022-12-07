# Radio Buttons

import tkinter as tk
import customtkinter as ctk

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
                           fg_color='grey',
                           corner_radius=0,
                           width=350,
                           height=50)
output_frame = ctk.CTkFrame(root,
                            corner_radius=0,
                            width=350,
                            height=300)

input_frame.pack(padx=20, pady=20)
output_frame.pack(padx=20, pady=(0,20))

# MAINLOOP
root.mainloop()
