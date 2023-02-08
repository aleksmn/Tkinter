import tkinter as tk
import customtkinter as ctk
import time
import locale




locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


class ClockFrame(ctk.CTkFrame):
    def __init__(self, container, primary_color=None):
        super().__init__(container)

        primary_color = "darkorchid1" if primary_color == None else primary_color
        secondary_color = "#39B5E0"

        primary_font = 'monospace', 18
        secondary_font = 'monospace', 40

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
        self.day_label.grid(row=1, column=0, sticky='e', padx=4)
        self.date_label.grid(row=1, column=1, sticky='w', padx=4)

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

        self.configure(padx=20, pady=20)

        self.clock_frame = ClockFrame(self, primary_color='magenta')
        self.clock_frame.grid(column=0, row=0)



# Запуск программы

if __name__ == "__main__":
    app = App()
    app.mainloop()
