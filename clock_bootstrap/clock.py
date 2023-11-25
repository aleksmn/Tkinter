import ttkbootstrap as ttk
import time

class ClockFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # Fonts
        primary_font = ('monospace', 18)
        secondary_font = ('monospace', 64)

        # 1) time
        self.time_label = ttk.Label(self, text="12:00", font=secondary_font, bootstyle="primary")
        self.time_label.grid(row=0, column=0, columnspan=2)

        # 2) day
        self.day_label = ttk.Label(self, text="Sunday", font=primary_font, bootstyle="danger")
        self.day_label.grid(row=1, column=0)

        # 3) date
        self.date_label = ttk.Label(self, text="19.11.2023", font=primary_font, bootstyle="danger")
        self.date_label.grid(row=1, column=1)

        self.update()


    def update(self):
        time_string = time.strftime("%H:%M:%S")
        self.time_label.configure(text=time_string)

        day_string = time.strftime("%A")
        self.day_label.configure(text=day_string.capitalize())

        date_string = time.strftime("%d %B %Y")
        self.date_label.configure(text=date_string)

        self.after(1000, self.update)




class App(ttk.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.configure(padx=40, pady=20)
        self.resizable(0, 0)

        self.clock = ClockFrame(self)
        self.clock.grid(column=0, row=0)




# Запуск программы
if __name__ == "__main__":
    app = App(title="My Clock", themename='minty')
    app.mainloop()