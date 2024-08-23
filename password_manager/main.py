import ttkbootstrap as ttk
from tkinter import Listbox, messagebox

from utils import *



def register():
    login_frame.destroy()

    register_frame = ttk.Frame(master=root) 
    register_frame.grid(pady=20,padx=40) 
    

    entry_label = ttk.Label(master=register_frame, text='Имя пользователя:') 
    entry_label.grid() 
    user_entry= ttk.Entry(master=register_frame) 
    user_entry.grid(pady=(0,12)) 
    
    pass_label = ttk.Label(master=register_frame, text='Пароль:') 
    pass_label.grid() 
    user_pass= ttk.Entry(master=register_frame, show="*") 
    user_pass.grid(pady=(0,12)) 

    pass_label_2 = ttk.Label(master=register_frame, text='Повторите пароль:') 
    pass_label_2.grid() 
    user_pass_2= ttk.Entry(master=register_frame, show="*") 
    user_pass_2.grid(pady=(0,12)) 
    

    register_button = ttk.Button(master=register_frame, text='Регистрация', style="secondary", command=create_user) 
    register_button.grid(pady=12, sticky="we") 
    



def login():
    login_frame.destroy()



# Создание главного окна
root = ttk.Window(themename="superhero")


FONT = ("monospace", 10, "bold")

root.title("Password Manager")
root.resizable(0, 0)

login_frame = ttk.Frame(master=root) 
login_frame.grid(pady=20,padx=40) 
  

entry_label = ttk.Label(master=login_frame, text='Имя пользователя:') 
entry_label.grid() 
user_entry= ttk.Entry(master=login_frame) 
user_entry.grid(pady=(0,12)) 
  
pass_label = ttk.Label(master=login_frame, text='Пароль:') 
pass_label.grid() 
user_pass= ttk.Entry(master=login_frame, show="*") 
user_pass.grid(pady=(0,12)) 
  

login_button = ttk.Button(master=login_frame, text='Вход', command=login) 
login_button.grid(pady=12, sticky="we") 

register_button = ttk.Button(master=login_frame, text='Регистрация', style="secondary", command=register) 
register_button.grid(pady=12, sticky="we") 
  




root.mainloop()