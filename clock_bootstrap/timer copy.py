import ttkbootstrap as ttk


# Создадим класс для таймера
class TimerFrame(ttk.Frame):
    def __init__(self, container):
        # конструктор родительского класса
        super().__init__(container)

        self.time_left = 0

        # Ввод времени
        self.time_entry = ttk.Entry(self)
        self.time_entry.grid(row=0, column=0, padx=10, pady=10)

        self.start_button = ttk.Button(self, text="Start", style="info", command=self.start_timer)
        self.start_button.grid(row=0, column=1, padx=(0, 10))

        self.stop_button = ttk.Button(self, text="Stop", bootstyle="danger")
        self.stop_button.grid(row=1, column=1, padx=(0, 10), pady=(0, 10))

        self.time_label = ttk.Label(self, text="00:00:00", font=('monospace', 18))
        self.time_label.grid(column=0, row=1)


    def start_timer(self):

        # ввод времени в формате ЧЧ:ММ:СС

        self.time_left = self.time_entry.get()

        self.time_left = int(self.time_left)
        
        self.update_timer()



    def update_timer(self):

        if self.time_left > 0:
            self.time_left -= 1
            # Выводим время на экран
            self.time_label.configure(text=self.time_left)
            self.after(1000, self.update_timer)




class App(ttk.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.resizable(0, 0)

        self.timer = TimerFrame(self)
        self.timer.grid(row=0, column=0)



# Запуск программы
if __name__ == "__main__":
    app = App()
    app.mainloop()