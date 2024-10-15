# Арсений
import customtkinter as ctk

class ColorFrame(ctk.CTkFrame):
    def __init__(self, container):
        super().__init__(container)

        self.red_value, self.green_value, self.blue_value = '00', '00', '00'

        self.selected_color = '#' + self.red_value + self.green_value + self.blue_value
        # Код цвета #000000 ---> #FFFFFF

        # Цветовой квадрат
        self.color_box = ctk.CTkLabel(self, fg_color=self.selected_color, text='', height=100, width=100)
        self.color_box.grid(row=0, column=0, columnspan=2, padx=35, pady=10)

        # Вывод кода цвета
        self.color_hex = ctk.CTkEntry(self, justify='center', width=100)
        self.color_hex.insert('end', self.selected_color)

        self.color_hex.grid(row=1, column=0, columnspan=2)

        # Слайдеры
        # слайдер для красного цвета
        self.red_label = ctk.CTkLabel(self, text="R")
        self.red_slider = ctk.CTkSlider(self, from_=0, to=255)

        self.red_label.grid(row=2, column=0, padx=(5, 0))
        self.red_slider.grid(row=2, column=1, padx=5)

        # слайдер для зеленого цвета


        # слайдер для синего цвета



# Точка входа в программу
if __name__ == "__main__":
    app = ctk.CTk()
    app.title('Color')
    
    cf = ColorFrame(app)
    cf.grid(column=0, row=0)

    app.mainloop()
