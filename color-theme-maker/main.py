'''Color Theme Maker'''
import tkinter as tk
import customtkinter as ctk

from color_frame import ColorFrame


# Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("dark-blue")



class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Color Themes')

        try:
            self.iconphoto(True, tk.PhotoImage(file='bulb-icon.png'))
        except:
            pass
        
        self.configure(padx=10, pady=10)

        options = {'padx': 10, 'pady': 10}

        self.color_frame = ColorFrame(self)
        self.color_frame.grid(column=0, row=0, **options)
        self.color2_frame = ColorFrame(self)
        self.color2_frame.grid(column=1, row=0, **options)
        self.color3_frame = ColorFrame(self)
        self.color3_frame.grid(column=2, row=0, **options)
        self.color4_frame = ColorFrame(self)
        self.color4_frame.grid(column=3, row=0, **options)


if __name__ == "__main__":

    app = App()
    app.mainloop()
