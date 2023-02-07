import customtkinter as ctk
import tkinter as tk
import time
import locale


locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Time waits for no one')
        self.configure(padx=20, pady=20)

        try:
            self.iconphoto(True, tk.PhotoImage(file='icon.png'))

        except:
            pass
