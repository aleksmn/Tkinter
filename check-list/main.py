'''Simple Text Editor'''
import tkinter as tk
import customtkinter as ctk

# Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("light")
# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("dark-blue")


# Define Window
root = ctk.CTk()
root.title("Check List")
root.iconphoto(True, tk.PhotoImage(file='logo.png'))
root.geometry('500x500')

# Fonts and Colors
my_font = ('sans-serif', 14)
primary_color = 'slateblue'
secondary_color = 'orange'



# Grid layout

## Columns
root.grid_columnconfigure((0,1), weight=1)

## Rows


# Widgets

list_entry = ctk.CTkEntry(root, width=200, font=my_font)
list_add_button = ctk.CTkButton(root, width=200, text="Add Item", font=my_font)

list_entry.grid(row='0', column='0', padx=(0, 20), pady=20)
list_add_button.grid(row='0', column='1')


my_listbox = tk.Listbox(root, borderwidth=0, height=14)
my_listbox.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=20)


# Buttons
list_remove_button = ctk.CTkButton(root, text='Remove Item')
list_clear_button = ctk.CTkButton(root, text='Clear List')
save_button = ctk.CTkButton(root, text='Save List')
quit_button = ctk.CTkButton(root, text='Quit')


list_remove_button.grid(row=2, column=0, pady=20)
list_clear_button.grid(row=2, column=1, pady=20)
save_button.grid(row=3, column=0)
quit_button.grid(row=3, column=1)


# Start Mainloop
root.mainloop()
