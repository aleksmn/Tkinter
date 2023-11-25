import ttkbootstrap as ttk
import time




# Создаем класс для таймера

class TimerFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # Виджеты
        self.time_entry = ttk.Entry(self)
        self.time_entry.grid(row=0, column=0, padx=10, pady=10)

        self.start_button = ttk.Button(self, text="Start", command=self.start)
        self.start_button.grid(row=0, column=1, padx=(0, 10))

        self.stop_button = ttk.Button(self, text="Stop", bootstyle="danger")
        self.stop_button.grid(row=1, column=1, padx=(0, 10), pady=(0, 10))

        self.time_label = ttk.Label(self, text="00:00:00", font=('monospace', 18))
        self.time_label.grid(column=0, row=1)


    def start(self):
        self.stop_loop = False
        hours, minutes, seconds = 0, 0, 0
        time_string = self.time_entry.get().split(":")
        if len(time_string) == 3:
            hours = int(time_string[0])
            minutes = int(time_string[1])
            seconds = int(time_string[2])

        elif len(time_string) == 2:
            minutes = int(time_string[0])
            seconds = int(time_string[1])

        elif len(time_string) == 1:
            seconds = int(time_string[0])
            
        else:
            print("Неверный формат ввода")
            return







class App(ttk.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.resizable(0, 0)
        
        self.timer = TimerFrame(self)
        self.timer.grid(column=0, row=0)



# Запуск программы
if __name__ == "__main__":
    app = App(title="My Timer", themename='minty', minsize=(100, 0))
    app.mainloop()