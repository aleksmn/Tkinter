import tkinter as tk
import customtkinter as ctk
import time
import locale
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


class ClockFrame(ctk.CTkFrame):
    def __init__(self, container, primary_color=None):
        super().__init__(container)

        primary_color = "darkorchid1" if primary_color == None else primary_color
        secondary_color = "#39B5E0"

        primary_font = 'monospace', 30
        secondary_font = 'monospace', 160

        self.configure(fg_color="transparent")

        # Widgets

        self.time_label = ctk.CTkLabel(self,
                                       font=secondary_font,
                                       text_color=primary_color)

        self.day_label = ctk.CTkLabel(self,
                                      font=primary_font,
                                      text_color=secondary_color)

        self.date_label = ctk.CTkLabel(self,
                                       font=primary_font,
                                       text_color=secondary_color)

        self.time_label.grid(row=0, column=0, columnspan=2)
        self.day_label.grid(row=1, column=0, sticky='e', padx=20)
        self.date_label.grid(row=1, column=1, sticky='w', padx=20)

        self.update()

    def update(self):
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

        self.title('Time waits for no one')
        self.configure(padx=20, pady=20)
        self.iconphoto(True, tk.PhotoImage(file=dir_path+'/icon.png'))

        self.clock_frame = ClockFrame(self)
        self.clock_frame.grid(column=0, row=0, padx=40, pady=40)

        self.clock_frame2 = ClockFrame(self, primary_color='magenta')
        self.clock_frame2.grid(column=0, row=2, padx=40, pady=40)

        self.clock_frame2 = ClockFrame(self, primary_color='cyan')
        self.clock_frame2.grid(column=0, row=3, padx=40, pady=40)






# Запуск программы
app = App()
app.mainloop()
