import tkinter as tk
import customtkinter as ctk
import time
from pytz import timezone
from datetime import datetime
import locale
import os


dir_path = os.path.dirname(os.path.realpath(__file__))

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


class ClockFrame(ctk.CTkFrame):
    def __init__(self, container, primary_color=None, tz=None, title=None):
        super().__init__(container)

        self.tz = tz

        # Настраиваем цвет по умолчанию, то есть, если цвет не передан в качестве аргумента
        primary_color = "darkorchid1" if primary_color == None else primary_color
        secondary_color = "#39B5E0"
        primary_font = 'monospace', 28
        secondary_font = 'monospace', 100

        self.configure(fg_color="transparent")

        # Widgets
        if title != None:
            self.title_label = ctk.CTkLabel(self,
                                            text=title,
                                            font=primary_font,
                                            text_color=primary_color)
            self.title_label.grid(row=0, column=0, columnspan=2)

        self.time_label = ctk.CTkLabel(self,
                                       font=secondary_font,
                                       text_color=primary_color)

        self.day_label = ctk.CTkLabel(self,
                                      font=primary_font,
                                      text_color=secondary_color)

        self.date_label = ctk.CTkLabel(self,
                                       font=primary_font,
                                       text_color=secondary_color)

        self.time_label.grid(row=1, column=0, columnspan=2)
        self.day_label.grid(row=2, column=0, sticky='e', padx=20)
        self.date_label.grid(row=2, column=1, sticky='w', padx=20)

        self.update()

    def get_time(self):
        if self.tz == None:
            return datetime.now()
        else:
            # now_utc = datetime.now(timezone('UTC'))
            # return now_utc.astimezone(timezone(self.tz))
            return datetime.now(timezone(self.tz))
        


    def update(self):
        time = self.get_time()
        time_string = time.strftime("%H:%M:%S")
        self.time_label.configure(text=time_string)

        day_string = time.strftime("%A")
        self.day_label.configure(text=day_string)

        date_string = time.strftime("%d %B %Y")
        self.date_label.configure(text=date_string)

        self.after(1000, self.update)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode('dark')

        self.title('Time waits for no one')
        self.configure(padx=20, pady=20)
        self.iconphoto(True, tk.PhotoImage(file=dir_path+'/icon.png'))

        self.clock_frame = ClockFrame(self,
                                      tz='Europe/Moscow',
                                      title='Москва')
        self.clock_frame.grid(column=0, row=0, padx=40, pady=40)

        self.clock_frame2 = ClockFrame(self,
                                       primary_color='magenta',
                                       tz='Asia/Novosibirsk',
                                       title='Новосибирск')
        self.clock_frame2.grid(column=0, row=2, padx=40, pady=40)

        self.clock_frame3 = ClockFrame(self,
                                       primary_color='cyan',
                                       tz='Asia/Vladivostok',
                                       title='Владивосток')
        self.clock_frame3.grid(column=0, row=3, padx=40, pady=40)


# Запуск программы
app = App()
app.mainloop()
