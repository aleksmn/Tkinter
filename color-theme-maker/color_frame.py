import customtkinter as ctk

class ColorFrame(ctk.CTkFrame):

    def __init__(self, container):
        super().__init__(container)

        self.red_value, self.green_value, self.blue_value = '00', '00', '00'

        self.selected_color = '#' + self.red_value + self.green_value + self.blue_value

        # Define Layout

        self.color_box = ctk.CTkLabel(
            self, fg_color='black', text='', height=100, width=100)
        self.color_hex = ctk.CTkEntry(self, justify='center', width=100)
        self.color_hex.insert('end', "#000000")

        self.color_box.grid(row=0, column=0, columnspan=2, padx=35, pady=10)
        self.color_hex.grid(row=1, column=0, columnspan=2,)

        # Input frame.

        # RED
        self.red_label = ctk.CTkLabel(self, text="R")
        self.red_slider = ctk.CTkSlider(
            self, from_=0, to=255, orientation='horizontal', command=lambda value: self.get_value(value, 'red'))
        self.red_label = ctk.CTkLabel(self, text="R")
        self.red_slider.set(0)

        # GREEN
        self.green_label = ctk.CTkLabel(self, text="G")
        self.green_slider = ctk.CTkSlider(
            self, from_=0, to=255, orientation='horizontal', command=lambda value: self.get_value(value, 'green'))
        self.green_slider.set(0)

        # BLUE
        self.blue_label = ctk.CTkLabel(self, text="B")
        self.blue_slider = ctk.CTkSlider(
            self, from_=0, to=255, orientation='horizontal', command=lambda value: self.get_value(value, 'blue'))
        self.blue_slider.set(0)

        # Размещаем все элементы:

        self.red_label.grid(row=2, column=0, sticky='W', padx=(5, 0))
        self.red_slider.grid(row=2, column=1, sticky='W', padx=5)

        self.green_label.grid(row=3, column=0, sticky='W', padx=(5, 0))
        self.green_slider.grid(row=3, column=1, sticky='W', padx=5)

        self.blue_label.grid(row=4, column=0, sticky='W', padx=(5, 0))
        self.blue_slider.grid(row=4, column=1, sticky='W', padx=5)

    def get_value(self, value, color):
        """Get current value for red and update color box"""

        # print(value, color)
        value = hex(int(value))
        value = value.lstrip('0x')
        value = value.zfill(2)

        if color == 'red':
            self.red_value = value
        if color == 'green':
            self.green_value = value
        if color == 'blue':
            self.blue_value = value
        

        self.update_color()



    def update_color(self):
        # print(red_value, green_value, blue_value)
        self.selected_color = f'#{self.red_value}{self.green_value}{self.blue_value}'
        self.color_box.configure(fg_color=self.selected_color)
        self.color_hex.delete(0, 'end')
        self.color_hex.insert(0, self.selected_color)

    def get_color(self):
        return self.selected_color


    def set_color(self, color):

        r, g, b = color[1:3], color[3:5], color[5:7]
        self.red_value, self.green_value, self.blue_value = r, g, b

        self.red_slider.set(int(r, 16))
        self.green_slider.set(int(g, 16))
        self.blue_slider.set(int(b, 16))

        self.update_color()


if __name__ == "__main__":

    app = ctk.CTk()
    app.title('Color')
    cf = ColorFrame(app)
    cf.grid(column=0, row=0)
    cf.set_color('#660000')
    
    app.mainloop()
