'''Simple Text Editor'''
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import customtkinter as ctk

# Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("dark-blue")


# Функции

def open_file():
    '''Открываем файл для редактирования'''

    filepath = askopenfilename(
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("0.0", tk.END)

    with open(filepath, "r", encoding='utf-8') as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    root.title(f"Простой текстовый редактор - {filepath}")



def save_file():
    '''Сохраняем текущий файл как новый файл.'''

    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("Python", "*.py"), ("All files", "*.*")],
    )

    if not filepath:
        return

    with open(filepath, "w", encoding='utf-8') as output_file:
        text = txt_edit.get("0.0", tk.END)
        output_file.write(text)

    root.title(f"Простой текстовый редактор - {filepath}")






root = ctk.CTk()
root.title("Простой текстовый редактор")

try:
    root.iconphoto(True, tk.PhotoImage(file='icon.png'))
except:
    pass

# Разметка окна
root.rowconfigure(0, minsize=500, weight=1)
root.columnconfigure(1, minsize=500, weight=1)


# Виджеты

txt_edit = ctk.CTkTextbox(root)
fr_buttons = ctk.CTkFrame(root)

fr_buttons.grid(row=0, column=0, sticky="ns", padx=20, pady=20)
txt_edit.grid(row=0, column=1, sticky="nsew", padx=(0, 20), pady=20)



# Кнопки
btn_open = ctk.CTkButton(fr_buttons, text="Открыть", command=open_file)

btn_save = ctk.CTkButton(fr_buttons, text="Сохранить как...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

btn_save.grid(row=1, column=0, sticky="ew", padx=10)




root.mainloop()
