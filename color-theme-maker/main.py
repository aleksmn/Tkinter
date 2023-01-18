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


# Define Window
root = ctk.CTk()
root.title("Colors")
try:
    root.iconphoto(True, tk.PhotoImage(file='bulb-icon.png'))
except:
    pass
root.configure(padx=20, pady=20)


# Functions
red_value, green_value, blue_value = '00', '00', '00'


def get_red(value):
    """Get current value for red and update color box"""
    global red_value
    red_value = hex(int(value))
    red_value = red_value.lstrip('0x')
    red_value = red_value.zfill(2)
    # print(f'{red_value=}')
    update_color()


def get_green(value):
    """Get current value for green and update color box"""
    global green_value
    green_value = hex(int(value))
    green_value = green_value.lstrip('0x')
    green_value = green_value.zfill(2)
    # print(f'{green_value=}')
    update_color()


def get_blue(value):
    """Get current value for blue and update color box"""
    global blue_value
    blue_value = hex(int(value))
    blue_value = blue_value.lstrip('0x')
    blue_value = blue_value.zfill(2)
    # print(f'{blue_value=}')
    update_color()

def update_color():
    # print(red_value, green_value, blue_value)
    selected_color = f'#{red_value}{green_value}{blue_value}'
    color_box.configure(fg_color=selected_color)
    color_hex.delete(0, 'end')
    color_hex.insert(0, selected_color)




#Define Layout
color_frame = ctk.CTkFrame(root)
input_frame = ctk.CTkFrame(root)


color_frame.pack(fill='both', expand=True, pady=(0,10))
input_frame.pack(fill='both', expand=True, pady=(0,10))





#Create the color box and color labels
color_box = ctk.CTkLabel(color_frame, fg_color='black', text='', height=100, width=100)
color_hex = ctk.CTkEntry(color_frame)
color_hex.insert('end', "#000000")
#Put the color box and labels on the frame.
color_box.grid(row=0, column=0, padx=35, pady=10)
color_hex.grid(row=1, column=0)

color_frame.grid_columnconfigure(0, weight=1)


#Setting up the input frame.
#Create the labels, sliders, and buttons for each color RGB
# RED
red_label = ctk.CTkLabel(input_frame, text="R")
red_slider = ctk.CTkSlider(input_frame, from_=0, to=255, orientation='horizontal', command=get_red)
red_label = ctk.CTkLabel(input_frame, text="R")
red_slider.set(0)
# red_button = ctk.CTkButton(input_frame, text="Red")

# GREEN
green_label = ctk.CTkLabel(input_frame, text="G")
green_slider = ctk.CTkSlider(input_frame, from_=0, to=255, orientation='horizontal', command=get_green)
green_slider.set(0)
# green_button = ctk.CTkButton(input_frame, text="Green")


# BLUE
blue_label = ctk.CTkLabel(input_frame, text="B")
blue_slider = ctk.CTkSlider(input_frame, from_=0, to=255, orientation='horizontal', command=get_blue)
blue_slider.set(0)
# blue_button = ctk.CTkButton(input_frame, text="Blue")


#Put labels, sliders, and buttons on to the frame.

red_label.grid(row=0, column=0, sticky='W')
red_slider.grid(row=0, column=1, sticky='W')
# red_button.grid(row=2, column=0, padx=5, pady=5)

green_label.grid(row=1, column=0, sticky='W')
green_slider.grid(row=1, column=1, sticky='W')
# green_button.grid(row=2, column=1, padx=5, pady=5)

blue_label.grid(row=2, column=0, sticky='W')
blue_slider.grid(row=2, column=1, sticky='W')
# blue_button.grid(row=2, column=2, padx=5, pady=5)

root.mainloop()
