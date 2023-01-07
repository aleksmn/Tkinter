'''Color Theme Maker'''
import tkinter as tk
import customtkinter as ctk

# Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("light")
# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("dark-blue")


# Fonts and Colors
my_font = ('sans-serif', 14)
primary_color = 'slateblue'
secondary_color = 'orange'


# Define Window
root = ctk.CTk()
root.title("Check List")
root.iconphoto(True, tk.PhotoImage(file='bulb-icon.png'))
root.configure(padx=20, pady=20)


# Functions




#Define Layout
color_frame = ctk.CTkFrame(root)
input_frame = ctk.CTkFrame(root)
output_frame = ctk.CTkFrame(root)

color_frame.pack(fill='both', expand=True, pady=(0,10))
input_frame.pack(fill='both', expand=True, pady=(0,10))
output_frame.pack(fill='both', expand=True)




#Create the color box and color labels
color_box = ctk.CTkLabel(color_frame, fg_color='black', text='', height=100, width=100)
color_hex = ctk.CTkLabel(color_frame, text='#000000')
#Put the color box and labels on the frame.
color_box.grid(row=0, column=0, padx=35, pady=10)
color_hex.grid(row=1, column=0)

color_frame.grid_columnconfigure(0, weight=1)


#Setting up the input frame.
#Create the labels, sliders, and buttons for each color RGB
# RED
red_label = ctk.CTkLabel(input_frame, text="R")
red_slider = ctk.CTkSlider(input_frame, from_=0, to=255, orientation='horizontal')
red_button = ctk.CTkButton(input_frame, text="Red")

# GREEN
green_label = ctk.CTkLabel(input_frame, text="G")
green_slider = ctk.CTkSlider(input_frame, from_=0, to=255, orientation='horizontal')
green_button = ctk.CTkButton(input_frame, text="Green")


# BLUE
blue_label = ctk.CTkLabel(input_frame, text="B")
blue_slider = ctk.CTkSlider(input_frame, from_=0, to=255, orientation='horizontal')
blue_button = ctk.CTkButton(input_frame, text="Blue")


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
