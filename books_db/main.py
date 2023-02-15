import tkinter as tk
import customtkinter as ctk

from db import DB


# Создаем объект класса DB
db = DB()

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")


class LibraryFrame(ctk.CTkFrame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        primary_color = "darkorchid1"
        secondary_color = "slateblue"
        primary_font = 'monospace', 18

        self.configure(fg_color='transparent')

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        # Лейблы

        self.l1 = ctk.CTkLabel(self, text="Название",
                               text_color=secondary_color, font=primary_font)

        self.l2 = ctk.CTkLabel(self, text="Автор",
                               text_color=secondary_color, font=primary_font)

        self.l3 = ctk.CTkLabel(self, text="Год",
                               text_color=secondary_color, font=primary_font)

        self.l1.grid(row=0, column=0, sticky='w', padx=20, pady=10)
        self.l2.grid(row=0, column=3, sticky='w', padx=(0, 20))
        self.l3.grid(row=0, column=5, sticky='w', padx=(0, 20))

        # Поля для ввода

        self.title_text = ctk.StringVar()
        # taking input from the user in the grid and storing it in a string variable
        self.e1 = ctk.CTkEntry(self, textvariable=self.title_text)

        self.author_text = ctk.StringVar()  # taking author name input
        self.e2 = ctk.CTkEntry(self, textvariable=self.author_text)

        self.isbn_text = ctk.StringVar()  # taking isbn input
        self.e3 = ctk.CTkEntry(self, textvariable=self.isbn_text)

        self.e1.grid(row=1, column=0, columnspan=3, sticky="we", padx=20)
        self.e2.grid(row=1, column=3, columnspan=2, sticky="we", padx=(0, 20))
        self.e3.grid(row=1, column=5, sticky="we", padx=(0, 20))

        # # LISTBOX

        self.my_listbox = tk.Listbox(self, borderwidth=0, bg=self['bg'])
        self.my_listbox.grid(row=2, column=0, columnspan=6,
                             sticky='ew', padx=20, pady=20)

        # # Scrollbar
        self.my_scrollbar = ctk.CTkScrollbar(
            self, command=self.my_listbox.yview)
        self.my_scrollbar.grid(row=2, column=6, sticky='nsw', pady=20)
        self.my_listbox.configure(yscrollcommand=self.my_scrollbar.set)

        # BUTTONS

        self.b1 = ctk.CTkButton(self, text="Просмотр")
        self.b1.grid(row=3, column=0, sticky="we", padx=(20, 10))

        self.b2 = ctk.CTkButton(self, text="Поиск")
        self.b2.grid(row=3, column=1, sticky="we", padx=(0, 10))

        self.b3 = ctk.CTkButton(self, text="Добавить")
        self.b3.grid(row=3, column=2, sticky="we", padx=(0, 10))

        self.b4 = ctk.CTkButton(self, text="Обновить")
        self.b4.grid(row=3, column=3, sticky="we", padx=(0, 10))

        self.b5 = ctk.CTkButton(self, text="Удалить")
        self.b5.grid(row=3, column=4, sticky="we", padx=(0, 10))

        self.b6 = ctk.CTkButton(self, text="Закрыть", command=container.destroy)
        self.b6.grid(row=3, column=5, sticky="we", padx=(0, 10))




class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('My Books')
        self.configure(padx=20, pady=20)
        self.minsize(600, 0)
        self.maxsize(800, 0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.library_frame = LibraryFrame(container=self)
        self.library_frame.grid(
            row=0, column=0, padx=20, pady=20, sticky="nsew")


if __name__ == "__main__":
    App().mainloop()
