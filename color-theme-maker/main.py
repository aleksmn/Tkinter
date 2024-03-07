'''Color Theme Maker'''
import tkinter as tk
import customtkinter as ctk

from color_frame import ColorFrame

# Modes: "System" (standard), "Dark", "Light"
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
        self.menu.configure(bg='#221f1e', fg='white',
                            border=0, font=('sans-serif', 9), activebackground='lightgrey')
        self.configure(menu=self.menu)
        self.menu.add_command(label='Сохранить', command=self.save_colors)
        self.menu.add_command(label='Вернуть цвета', command=self.load_colors)

        self.load_colors()

        # Добавляем действия на закрытие окна программы
        self.protocol("WM_DELETE_WINDOW", self.on_closing)


    def save_colors(self):

        for cf in self.color_frames:
            print(cf.get_color())
        
        # Записываем в файл
        with open('my_colors.txt', 'w', encoding='utf-8') as f:
            for cf in self.color_frames:
                f.write(cf.get_color() + '\n')

        print("Сохранено в файл my_colors.txt")


    def load_colors(self):
        try:
            with open('my_colors.txt', 'r', encoding='utf-8') as f:
                data = f.read()
                colors = data.split()
                for i, cf in enumerate(self.color_frames):
                    cf.set_color(colors[i])
        except:
            pass


    def on_closing(self):
        # По закрытию окна 
        # сохраняем цвета
        self.save_colors()
        # закрываем окно программы
        self.destroy()







if __name__ == "__main__":

    app = App()
    app.mainloop()
