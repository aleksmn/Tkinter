import ttkbootstrap as ttk
import time




# Создаем класс для таймера

class TimerFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # Виджеты
        self.time_entry = ttk.Entry(self)
        self.time_entry.grid(row=0, column=0, padx=10, pady=10)

        self.start_button = ttk.Button(self, text="Start")
        self.start_button.grid(row=0, column=1, padx=(0, 10))

        self.stop_button = ttk.Button(self, text="Stop", bootstyle="danger")
        self.stop_button.grid(row=1, column=1, padx=(0, 10), pady=(0, 10))






class App(ttk.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.resizable(0, 0)
        
        self.timer = TimerFrame(self)
        self.timer.grid(column=0, row=0)



# Запуск программы
if __name__ == "__main__":
    app = App(title="My Timer", themename='minty', minsize=(200, 0))
    app.mainloop()