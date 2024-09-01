import tkinter as tk
import customtkinter as ctk

from color_frame import ColorFrame


ctk.set_appearance_mode("light")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Color Theme Maker')

        self.configure(padx=10, pady=10)
        self.resizable(0, 0)

        self.color_frames = []

        for i in range(4):
            cf = ColorFrame(self)
            cf.grid(column=i, row=0, padx=10, pady=10)
            self.color_frames.append(cf)





# Запус программы
if __name__ == "__main__":

    app = App()
    app.mainloop()
