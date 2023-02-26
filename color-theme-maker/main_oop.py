'''Color Theme Maker'''
import tkinter as tk
import customtkinter as ctk

# Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("dark-blue")


# Fonts and Colors
my_font = ('sans-serif', 14)
primary_color = 'slateblue'
secondary_color = 'orange'


class ColorFrame(ctk.CTkFrame):

    def __init__(self, container):
        super().__init__(container)

        self.red_value, self.green_value, self.blue_value = '00', '00', '00'

        # Define Layout

        self.color_box = ctk.CTkLabel(self, fg_color='black', text='', height=100, width=100)
        self.color_hex = ctk.CTkEntry(self, justify='center', width=100)
        self.color_hex.insert('end', "#000000")

        self.color_box.grid(row=0, column=0, columnspan=2, padx=35, pady=10)
        self.color_hex.grid(row=1, column=0, columnspan=2,)



        # Input frame.

        # RED
        self.red_label = ctk.CTkLabel(self, text="R")
        self.red_slider = ctk.CTkSlider(self, from_=0, to=255, orientation='horizontal', command=self.get_red)
        self.red_label = ctk.CTkLabel(self, text="R")
        self.red_slider.set(0)

        # GREEN
        self.green_label = ctk.CTkLabel(self, text="G")
        self.green_slider = ctk.CTkSlider(
            self, from_=0, to=255, orientation='horizontal', command=self.get_green)
        self.green_slider.set(0)

        # BLUE
        self.blue_label = ctk.CTkLabel(self, text="B")
        self.blue_slider = ctk.CTkSlider(self, from_=0, to=255, orientation='horizontal', command=self.get_blue)
        self.blue_slider.set(0)


        # Размещаем все элементы:

        self.red_label.grid(row=2, column=0, sticky='W', padx=(5, 0))
        self.red_slider.grid(row=2, column=1, sticky='W', padx=5)

        self.green_label.grid(row=3, column=0, sticky='W', padx=(5, 0))
        self.green_slider.grid(row=3, column=1, sticky='W', padx=5)

        self.blue_label.grid(row=4, column=0, sticky='W', padx=(5, 0))
        self.blue_slider.grid(row=4, column=1, sticky='W', padx=5)

    def get_red(self, value):
        """Get current value for red and update color box"""
        self.red_value = hex(int(value))
        self.red_value = self.red_value.lstrip('0x')
        self.red_value = self.red_value.zfill(2)
        # print(f'{self.red_value=}')
        self.update_color()

    def get_green(self, value):
        """Get current value for green and update color box"""
        self.green_value = hex(int(value))
        self.green_value = self.green_value.lstrip('0x')
        self.green_value = self.green_value.zfill(2)
        # print(f'{self.green_value=}')
        self.update_color()

    def get_blue(self, value):
        """Get current value for blue and update color box"""
        self.blue_value = hex(int(value))
        self.blue_value = self.blue_value.lstrip('0x')
        self.blue_value = self.blue_value.zfill(2)
        # print(f'{self.blue_value=}')
        self.update_color()

    def update_color(self):
        # print(red_value, green_value, blue_value)
        selected_color = f'#{self.red_value}{self.green_value}{self.blue_value}'
        self.color_box.configure(fg_color=selected_color)
        self.color_hex.delete(0, 'end')
        self.color_hex.insert(0, selected_color)


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
