import ttkbootstrap as ttk

from clock import ClockFrame
from timer import TimerFrame


class App(ttk.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.resizable(0, 0)

        self.configure(padx=20, pady=20)

        self.clock = ClockFrame(self)
        self.clock.grid(row=0, column=0)

        self.timer = TimerFrame(self)
        self.timer.grid(row=1, column=0, pady=(20, 0))

        self.timer2 = TimerFrame(self)
        self.timer2.grid(row=2, column=0, pady=(20, 0))

if __name__ == "__main__":
    app = App(title="Best Timer", themename='superhero')
    app.mainloop()