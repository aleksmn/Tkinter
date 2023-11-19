import ttkbootstrap as ttk


class ClockFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # Fonts
        primary_font = ('monospace', 12)
        secondary_font = ('monospace', 44)

        # 1) time
        self.time_label = ttk.Label(self, text="12:00", font=secondary_font)
        self.time_label.grid(row=0, column=0, columnspan=2)

        # 2) day
        self.day_label = ttk.Label(self, text="Sunday", font=primary_font)
        self.day_label.grid(row=1, column=0)

        # 3) date
        self.date_label = ttk.Label(self, text="19.11.2023", font=primary_font)
        self.date_label.grid(row=1, column=1)






class App(ttk.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.configure(padx=40, pady=20)
        self.resizable(0, 0)

        self.clock = ClockFrame(self)
        self.clock.grid(column=0, row=0)




# Запуск программы
if __name__ == "__main__":
    app = App(title="My Clock", themename='superhero')
    app.mainloop()