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

        self.color_frame_1 = ColorFrame(self)
        self.color_frame_1.grid(column=0, row=0, **options)
        self.color_frame_2 = ColorFrame(self)
        self.color_frame_2.grid(column=1, row=0, **options)
        self.color_frame_3 = ColorFrame(self)
        self.color_frame_3.grid(column=2, row=0, **options)
        self.color_frame_4 = ColorFrame(self)
        self.color_frame_4.grid(column=3, row=0, **options)


        # # Меню
        # self.menu = tk.Menu(self)
        # self.menu.configure(bg='#221f1e', fg='white',
        #                     border=0, font=('sans-serif', 9), activebackground='lightgrey')
        # self.configure(menu=self.menu)
        # self.menu.add_command(label='Сохранить', command=self.save_colors)


    def save_colors(self):
        colors = [
            self.color_frame_1.get_color(),
            self.color_frame_2.get_color(),
            self.color_frame_3.get_color(),
            self.color_frame_4.get_color(),
        ]

        # for c in colors:
        #     print(c)

        with open('my_colors.txt', 'w', encoding='utf-8') as f:
            for c in colors:
                f.write(c + '\n')

        





if __name__ == "__main__":

    app = App()
    app.mainloop()
