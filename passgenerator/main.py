import customtkinter as ctk
from generator import generate_password


print(generate_password())


root = ctk.CTk()

root.geometry('400x200')

root.title("Password Generator")


root.mainloop()