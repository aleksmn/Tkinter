import ttkbootstrap as ttk
from pytz import timezone
from datetime import datetime
import json

with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

TIMEZONES = config["timezones"]
THEMENAME = config["themename"]

class ClockFrame(ttk.Frame):
    def __init__(self, container, tz=None, title=None):
        super().__init__(container)

        self.tz = tz
        self.title = title if title else tz

        # Fonts
        primary_font = ('monospace', 10)
        secondary_font = ('monospace', 34)

        if self.title:
            self.title_label = ttk.Label(self,
                                            text=self.title,
                                            font=primary_font)
            self.title_label.grid(row=0, column=0, columnspan=2)

        # time
        self.time_label = ttk.Label(self, text="12:00", font=secondary_font, bootstyle="primary")
        self.time_label.grid(row=1, column=0, columnspan=2)

        # day
        self.day_label = ttk.Label(self, text="Sunday", font=primary_font)
        self.day_label.grid(row=2, column=0)

        # date
        self.date_label = ttk.Label(self, text="19.11.2023", font=primary_font)
        self.date_label.grid(row=2, column=1)




        self.update()

    def get_time(self):
        if self.tz == None:
            return datetime.now()
        else:
            # now_utc = datetime.now(timezone('UTC'))
            # return now_utc.astimezone(timezone(self.tz))
            return datetime.now(timezone(self.tz))
        


    def update(self):
        time = self.get_time()
        time_string = time.strftime("%H:%M:%S")
        self.time_label.configure(text=time_string)

        day_string = time.strftime("%A").capitalize()
        self.day_label.configure(text=day_string)

        date_string = time.strftime("%d %b %Y")
        self.date_label.configure(text=date_string)

        self.after(1000, self.update)


class App(ttk.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.configure(padx=10, pady=10)
        self.resizable(0, 0)

    
        self.clock_list = []

        for item in TIMEZONES:
            self.clock_list.append(ClockFrame(self, tz=item["tz"], title=item["title"]))

        row_num = 0    
        for i, clock in enumerate(self.clock_list):
            
            if i > 0 and i % 4 == 0:
                row_num += 1

            clock.grid(row=row_num, column=i%4, padx=30, pady=30)


        
        # Icon Image
        self.iconbitmap('icon.ico')
        


        
# Запуск программы
if __name__ == "__main__":
    app = App(title="World Time", themename=THEMENAME)
    app.mainloop()