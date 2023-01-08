import customtkinter as ctk
import tkinter as tk
import time
import locale


locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')



# Main Window

root = ctk.CTk()
root.title('Time waits for no one')
root.configure(padx=20, pady=20)
try:
    root.iconphoto(True, tk.PhotoImage(file='icon.png'))
except:
    pass

primary_color = "darkorchid1"
secondary_color = "#39B5E0"


# Function

def update():
    time_string = time.strftime("%H:%M:%S")
    time_label.configure(text=time_string)

    day_string = time.strftime("%A")
    day_label.configure(text=day_string)

    date_string = time.strftime("%d %B %Y")
    date_label.configure(text=date_string)

    root.after(1000, update)



# Widgets

time_label = ctk.CTkLabel(root, font=('monospace', 160), text_color=primary_color)
time_label.grid(row=0, column=0, columnspan=2)

day_label = ctk.CTkLabel(root, font=('monospace', 30), text_color=secondary_color)
day_label.grid(row=1, column=0, sticky='e', padx=20)

date_label = ctk.CTkLabel(root, font=(
    'monospace', 30), text_color=secondary_color)
date_label.grid(row=1, column=1, sticky='w', padx=20)

update()

root.mainloop()
