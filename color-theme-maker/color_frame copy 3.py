import customtkinter as ctk

class ColorFrame(ctk.CTkFrame):

    def __init__(self, container):
        super().__init__(container)

        self.red_value, self.green_value, self.blue_value = '00', '00', '00'

        self.selected_color = '#' + self.red_value + self.green_value + self.blue_value

        # Цветовой квадрат
        self.color_box = ctk.CTkLabel(self, fg_color=self.selected_color, text='', height=100, width=100)
        self.color_box.grid(row=0, column=0, columnspan=2, padx=35, pady=10)

        # Вывод кода цвета в шестнадцатеричной системе
        self.color_hex = ctk.CTkEntry(self, justify='center', width=100)
        self.color_hex.insert('end', self.selected_color)

        self.color_hex.grid(row=1, column=0, columnspan=2)

        # Слайдеры
        # слайдер для красного цвета
        self.red_label = ctk.CTkLabel(self, text="R", text_color="red")
        self.red_slider = ctk.CTkSlider(self, from_=0, to=255, command=lambda value: self.get_value(value, "red"))
        self.red_label.grid(row=2, column=0, padx=(5, 0))
        self.red_slider.grid(row=2, column=1, padx=5)
        self.red_slider.set(0)

        # слайдер для зеленого цвета
        self.green_label = ctk.CTkLabel(self, text="G")
        self.green_slider = ctk.CTkSlider(self, from_=0, to=255, command=lambda value: self.get_value(value, "green"))
        self.green_label.grid(row=3, column=0, padx=(5, 0))
        self.green_slider.grid(row=3, column=1, padx=5)
        self.green_slider.set(0)

        # слайдер для синего цвета
        self.blue_label = ctk.CTkLabel(self, text="B")
        self.blue_slider = ctk.CTkSlider(self, from_=0, to=255, command=lambda value: self.get_value(value, "blue"))
        self.blue_label.grid(row=4, column=0, padx=(5, 0))
        self.blue_slider.grid(row=4, column=1, padx=5)
        self.blue_slider.set(0)


    def get_value(self, value, color):
        
        value = hex(int(value))
        
        print(value, color)



   
if __name__ == "__main__":

    app = ctk.CTk()
    app.title('Color')
    cf = ColorFrame(app)
    cf.grid(column=0, row=0)

    
    app.mainloop()
