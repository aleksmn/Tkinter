'''Simple Text Editor'''
import tkinter as tk
import customtkinter as ctk

# Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("dark-blue")


# Fonts and Colors
my_font = ('sans-serif', 14)
primary_color = 'slateblue'
secondary_color = 'orange'


# Define Window
root = ctk.CTk()
root.title("Check List")
root.iconphoto(True, tk.PhotoImage(file='logo.png'))
# root.geometry('500x500')
root.configure(padx=20, fg_color=primary_color)


# Functions

def add_item():
    '''Add item to the list box'''

    my_listbox.insert('end', list_entry.get())
    list_entry.delete(0, tk.END)





# Grid layout

# Columns
root.grid_columnconfigure((0, 1, 2, 3), weight=1)

# Rows


# Widgets

list_entry = ctk.CTkEntry(root, font=my_font, fg_color='gray', text_color='white')
list_add_button = ctk.CTkButton(root, text="Add Item", font=my_font, command=add_item)

list_entry.grid(row=0, column=0, columnspan=3,
                pady=20, padx=(0, 20), sticky='we')
list_add_button.grid(row=0, column=3)


my_listbox = tk.Listbox(root, borderwidth=0, height=14,
                        bg='gray', fg='white')
my_listbox.grid(row=1, column=0, columnspan=4, sticky='nsew')


my_scrollbar = ctk.CTkScrollbar(root, command=my_listbox.yview)
my_scrollbar.grid(row=1, column=3, sticky='nse')

my_listbox.configure(yscrollcommand=my_scrollbar.set)


# Buttons
list_remove_button = ctk.CTkButton(root, text='Remove Item')
list_clear_button = ctk.CTkButton(root, text='Clear List')
save_button = ctk.CTkButton(root, text='Save List')
quit_button = ctk.CTkButton(root, text='Quit')


list_remove_button.grid(row=2, column=0, pady=20)
list_clear_button.grid(row=2, column=1, padx=(20, 0))
save_button.grid(row=2, column=2, padx=(20, 0))
quit_button.grid(row=2, column=3, padx=(20, 0))


# Start Mainloop
root.mainloop()
