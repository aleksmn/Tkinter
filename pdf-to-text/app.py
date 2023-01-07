import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import os

# Для отладки:
# cwd = os.getcwd()
# print("Рабочая директория: ", cwd)
# print("Список файлов ", os.listdir(cwd))

root = tk.Tk()
root.title("Мудрый филин получает текст из PDF")

root.iconphoto(False, tk.PhotoImage(file='logo.png'))

canvas = tk.Canvas(root, width=500, height=300)
canvas.grid(columnspan=3, rowspan=3)

logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo

logo_label.grid(column=1, row=0)


# Инструкции
instructons = tk.Label(root, text="Уу-ху! Выбери PDF файл", font="Arial")
instructons.grid(columnspan=3, column=0, row=1)


# Функция открытия документа

def open_file():
    # print("Открытие файла")
    browse_text.set("Загрузка...")
    file = askopenfile(parent=root, mode='rb',
                       title="Выбери файл. Уу-ху!", filetypes=[("Pdf file", "*.pdf")])
    if file:
        # print("Файл загружен!")
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        # print(page_content)

        text_box = tk.Text(root, height=8, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.grid(column=1, row=3)

        # Запись в файл
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(page_content)


# Кнопка Обзор
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text,
                       command=lambda: open_file(),
                       font="Arial",
                       bg="#20bebe",
                       fg="white",
                       height=2,
                       width=15)
                       
browse_text.set("Обзор")
browse_btn.grid(column=1, row=2)


canvas = tk.Canvas(root, width=500, height=200)
canvas.grid(columnspan=3)

root.mainloop()
