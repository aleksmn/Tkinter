import threading
import time
import customtkinter as ctk
from playsound import playsound

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

ctk.set_appearance_mode('dark')

# Создаем класс для таймера


class TimerFrame(ctk.CTkFrame):

    def __init__(self, container):
        super().__init__(container)

        self.time_entry = ctk.CTkEntry(self, font=('sans-serif', 20))
        self.time_entry.grid(row=0, column=0,  padx=10, pady=10)

        self.start_button = ctk.CTkButton(self,
                                          font=('sans-serif', 20),
                                          text="Старт",
                                          command=self.start_thread)
        self.start_button.grid(row=0, column=1, padx=10, pady=10)

        self.stop_button = ctk.CTkButton(self,
                                         font=('sans-serif', 20),
                                         text="Стоп",
                                         command=self.stop)
        self.stop_button.grid(row=1, column=1, padx=10, pady=(0, 10))

        self.time_label = ctk.CTkLabel(self,
                                       font=('sans-serif', 30),
                                       text="00:00:00")
        self.time_label.grid(row=1, column=0,  padx=10, pady=(0, 10))

        self.stop_loop = False

    def start_thread(self):
        t = threading.Thread(target=self.start)
        t.start()

    def start(self):
        self.stop_loop = False
        hours, minutes, seconds = 0, 0, 0
        string_split = self.time_entry.get().split(":")
        if len(string_split) == 3:
            hours = int(string_split[0])
            minutes = int(string_split[1])
            seconds = int(string_split[2])
        elif len(string_split) == 2:
            minutes = int(string_split[0])
            seconds = int(string_split[1])
        elif len(string_split) == 1:
            seconds = int(string_split[0])
        else:
            print("Неверный формат ввода")
            return

        full_seconds = hours * 3600 + minutes * 60 + seconds

        while full_seconds > 0 and not self.stop_loop:
            
            minutes, seconds = divmod(full_seconds, 60)
            hours, minutes = divmod(minutes, 60)

            self.time_label.configure(
                text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            
            full_seconds -= 1
            time.sleep(1)
            self.update()
            

        if not self.stop_loop:
            self.time_label.configure(text="00:00:00")
            print('Таймер закончен!')
            playsound(dir_path+"/alarm.wav")
            

    def stop(self):
        self.stop_loop = True
        self.time_label.configure(text="00:00:00")




class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # self.configure(padx=20, pady=20)

        self.clock_frame = TimerFrame(self)
        self.clock_frame.grid(column=0, row=0)




if __name__ == "__main__":
  app = App()
  app.mainloop()
