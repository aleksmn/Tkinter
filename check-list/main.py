'''Simple Text Editor'''
import tkinter as tk
import customtkinter as ctk

# Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("light")
# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("dark-blue")


root = ctk.CTk()
root.title("Check List")
root.iconphoto(True, tk.PhotoImage(file='logo.png'))
root.rowconfigure(0, minsize=500, weight=1)
root.columnconfigure(1, minsize=500, weight=1)


root.mainloop()
