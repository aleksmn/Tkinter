import tkinter as tk
import customtkinter as ctk
import time
import locale
import os


from clock import ClockFrame
from timer import TimerFrame

# Путь к папке запуска программы
dir_path = os.path.dirname(os.path.realpath(__file__))


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Time waits for no one')
        self.configure(padx=20, pady=20)
        self.iconphoto(True, tk.PhotoImage(file=dir_path+'/icon.png'))

        self.clock_frame = ClockFrame(self, primary_color='white')
        self.clock_frame.grid(column=0, row=0, padx=10, pady=10)

        self.clock_frame = TimerFrame(self)
        self.clock_frame.grid(column=0, row=1)


# Запуск программы
App().mainloop()
