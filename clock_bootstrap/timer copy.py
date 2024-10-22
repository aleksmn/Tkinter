import ttkbootstrap as ttk
import time



# Создаем класс для таймера
class TimerFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # Виджеты
        # Поле для ввода
        self.time_entry = ttk.Entry(self)
        self.time_entry.grid(row=0, column=0, padx=10, pady=10)

        ...





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