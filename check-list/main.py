'''Simple Text Editor'''
import tkinter as tk
import customtkinter as ctk

# Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("light")
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
root.configure(padx=20)


# Functions

def add_item():
    '''Добавляем строку в список'''
    my_listbox.insert('end', list_entry.get())
    list_entry.delete(0, tk.END)


def remove_item():
    """Удаляем строку из списка"""
    my_listbox.delete(tk.ANCHOR)


def clear_list():
    """Удаляем все из списка"""
    my_listbox.delete(0, tk.END)


def save_list():
    """Сохраняем список в текстовый файл"""
    with open('checklist.txt', 'w', encoding='utf-8') as f:
        # listbox.get() возвращает кортеж (tuple)
        list_tuple = my_listbox.get(0, tk.END)
        for item in list_tuple:
            # Добавляем перенос на новую строку
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item + '\n')


def open_list():
    """Открываем список из файла, если он есть"""
    try:
        with open('checklist.txt', 'r') as f:
            for line in f:
                my_listbox.insert(tk.END, line)
    except:
        return

# Grid layout


# Columns
root.grid_columnconfigure((0, 1, 2, 3), weight=1)

# Rows


# Widgets

list_entry = ctk.CTkEntry(root, font=my_font)
list_add_button = ctk.CTkButton(
    root, text="Add Item", font=my_font, command=add_item)

list_entry.grid(row=0, column=0, columnspan=3,
                pady=20, padx=(0, 20), sticky='we')
list_add_button.grid(row=0, column=3)


my_listbox = tk.Listbox(root, borderwidth=0, height=14, bg=root['bg'])
my_listbox.grid(row=1, column=0, columnspan=4, sticky='nsew')


my_scrollbar = ctk.CTkScrollbar(root, command=my_listbox.yview)
my_scrollbar.grid(row=1, column=3, sticky='nse')

my_listbox.configure(yscrollcommand=my_scrollbar.set)


# Buttons
list_remove_button = ctk.CTkButton(
    root, text='Remove Item', command=remove_item)
list_clear_button = ctk.CTkButton(root, text='Clear List', command=clear_list)
save_button = ctk.CTkButton(root, text='Save List', command=save_list)
quit_button = ctk.CTkButton(root, text='Quit', command=root.destroy)


list_remove_button.grid(row=2, column=0, pady=20)
list_clear_button.grid(row=2, column=1, padx=(20, 0))
save_button.grid(row=2, column=2, padx=(20, 0))
quit_button.grid(row=2, column=3, padx=(20, 0))

# Open List if available
open_list()

# Start Mainloop
root.mainloop()
