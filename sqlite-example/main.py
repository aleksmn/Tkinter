import tkinter as tk
import customtkinter as ctk

from db import DB


# Создаем объект класса DB
db = DB()


class LibraryFrame(ctk.CTkFrame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        primary_color = "darkorchid1"
        secondary_color = "slateblue"
        primary_font = 'monospace', 18

        # self.configure(fg_color='transparent')

        self.grid_columnconfigure((0,1,2,3), weight=1)


        #### Лейблы

        l1 = ctk.CTkLabel(self, text="Название",
                          text_color=secondary_color, font=primary_font)

        l2 = ctk.CTkLabel(self, text="Автор",
                          text_color=secondary_color, font=primary_font)

        l3 = ctk.CTkLabel(self, text="Год",
                          text_color=secondary_color, font=primary_font)

        l1.grid(row=0, column=0, sticky='w', padx=20, pady=10)
        l2.grid(row=0, column=1, sticky='w', padx=(0, 20))
        l3.grid(row=0, column=2, sticky='w', padx=(0, 20))

        # Поля для ввода

        title_text = ctk.StringVar()
        # taking input from the user in the grid and storing it in a string variable
        e1 = ctk.CTkEntry(self, textvariable=title_text)

        author_text = ctk.StringVar()  # taking author name input
        e2 = ctk.CTkEntry(self, textvariable=author_text)

        isbn_text = ctk.StringVar()  # taking isbn input
        e3 = ctk.CTkEntry(self, textvariable=isbn_text)

        e1.grid(row=1, column=0, sticky="we", padx=20)
        e2.grid(row=1, column=1, sticky="we", padx=(0, 20))
        e3.grid(row=1, column=2, sticky="we", padx=(0, 20))

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('My Books')
        self.configure(padx=20, pady=20)
        self.resizable(0, 0)
        self.geometry("800x400")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.library_frame = LibraryFrame(container=self)
        self.library_frame.grid(
            row=0, column=0, padx=20, pady=20, sticky="nsew")


if __name__ == "__main__":
    App().mainloop()
