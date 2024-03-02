'''Color Theme Maker'''
import tkinter as tk
import customtkinter as ctk

import os

from color_frame import ColorFrame


# Путь к папке запуска программы
dir_path = os.path.dirname(os.path.realpath(__file__))

# Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("light")
# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("dark-blue")



class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Color Theme Maker')

        try:
            self.iconphoto(True, tk.PhotoImage(file=dir_path + '/icon.png'))
        except:
            pass
        
        self.configure(padx=10, pady=10)
        self.resizable(0, 0)

        options = {'padx': 10, 'pady': 10}

        self.color_frames = []

        for i in range(4):
            cf = ColorFrame(self)
            cf.grid(column=i, row=0, **options)
            self.color_frames.append(cf)

        # self.color_frame_1 = ColorFrame(self)
        # self.color_frame_1.grid(column=0, row=0, **options)
        # self.color_frame_2 = ColorFrame(self)
        # self.color_frame_2.grid(column=1, row=0, **options)
        # self.color_frame_3 = ColorFrame(self)
        # self.color_frame_3.grid(column=2, row=0, **options)
        # self.color_frame_4 = ColorFrame(self)
        # self.color_frame_4.grid(column=3, row=0, **options)


        # # Меню
        self.menu = tk.Menu(self)
        self.menu.configure(bg='#221f1e', fg='white',
                            border=0, font=('sans-serif', 9), activebackground='lightgrey')
        self.configure(menu=self.menu)
        self.menu.add_command(label='Сохранить', command=self.save_colors)

        self.load_colors()


    def save_colors(self):

        for cf in self.color_frames:
            print(cf.get_color())
    
        with open(dir_path + '/my_colors.txt', 'w', encoding='utf-8') as f:
            for cf in self.color_frames:
                f.write(cf.get_color() + '\n')

        print("Сохранено в файл " + dir_path + '/my_colors.txt')


    def load_colors(self):
        try:
            with open(dir_path + '/my_colors.txt', 'r', encoding='utf-8') as f:
                data = f.read()
                colors = data.split()
                for i, cf in enumerate(self.color_frames):
                    cf.set_color(colors[i])
        except:
            pass


        





if __name__ == "__main__":

    app = App()
    app.mainloop()
