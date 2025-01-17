import ttkbootstrap as ttk
from playsound import playsound

#  pip install playsound==1.2.2

# mixkit.com
# alarm

# Создадим класс для таймера
class TimerFrame(ttk.Frame):
    def __init__(self, container):
        # конструктор родительского класса
        super().__init__(container)

        self.time_left = 0
        self.stop_loop = True

        # Ввод времени
        self.time_entry = ttk.Entry(self)
        self.time_entry.grid(row=0, column=0, padx=10, pady=10)

        self.start_button = ttk.Button(self, text="Start", style="info", command=self.start)
        self.start_button.grid(row=0, column=1, padx=(0, 10))

        self.stop_button = ttk.Button(self, text="Stop", bootstyle="danger", command=self.stop)
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
        
        # вычислим, сколько всего секунд
        self.time_left = hours * 3600 + minutes * 60 + seconds

        self.update_timer()

    
    def update_timer(self):

        if self.time_left == 0 and not self.stop_loop:
            self.time_label.configure(text="00:00:00")
            self.update()
            playsound("alarm.wav")


        elif self.time_left >= 0 and not self.stop_loop:
            # Получим часы, минуты и секунды
            hours = self.time_left // 3600
            minutes = self.time_left % 3600 // 60
            seconds = self.time_left % 60

            # Вывод времени
            self.time_label.configure(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

            # Ждем 1 секунду
            self.after(1000, self.update_timer)

            self.time_left -= 1
 


    def stop(self):
        self.stop_loop = True
        self.time_label.configure(text="00:00:00")


    

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