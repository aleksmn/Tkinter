import tkinter as tk
import customtkinter as ctk

# Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("blue")


# Создаем окно программы
root = ctk.CTk()
root.title("Функции")
root.iconphoto(True, tk.PhotoImage(file='logo.png'))
root.geometry('500x500')
root.resizable(0, 0)

# Определяем цвета и шрифт
primary_color = "orange"
secondary_color = "lightblue"
my_font = ('monospace', 14)


# Input Frame
input_frame = ctk.CTkFrame(root)
input_frame.pack(fill='both', padx=20, pady=20)

input_frame.columnconfigure(0, weight=3)
input_frame.columnconfigure(1, weight=1)


text_entry = ctk.CTkEntry(input_frame, font=my_font)
text_entry.grid(row=0, column=0, sticky='ew', padx=10, pady=10)

print_button = ctk.CTkButton(
    input_frame, text="Print!", font=my_font, hover_color=primary_color)
print_button.grid(row=0, column=1, sticky='ew', padx=(0, 10))



# Output frame

output_frame = ctk.CTkFrame(root)
output_frame.pack(fill='both', padx=20, pady=(0, 20))

root.mainloop()
