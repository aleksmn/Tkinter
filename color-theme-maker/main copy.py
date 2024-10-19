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

        # Меню
        self.menu = tk.Menu(self)
        self.configure(menu=self.menu)
        self.menu.add_command(label='Сохранить', command=self.save_colors)
        self.menu.add_command(label='Вернуть цвета', command=self.load_colors)

        # Загружаем цвета
        self.load_colors()


    def save_colors(self):
        
        for cf in self.color_frames:
            print(cf.get_color())


        # Записываем в файл
        with open('my_colors.txt', 'w', encoding='utf-8') as file:
            for cf in self.color_frames:
                file.write(cf.get_color() + '\n')


    def load_colors(self):
        try:
            with open('my_colors.txt', 'r', encoding='utf-8') as file:
                data = file.read()
                colors = data.split()

            i = 0
            for cf in self.color_frames:
                cf.set_color(colors[i])
                i += 1

        except FileNotFoundError:
            print("Файл с цветовой темой не найден")


# Запус программы
if __name__ == "__main__":

    app = App()
    app.mainloop()

    # Сохраняем цвета
    app.save_colors()
