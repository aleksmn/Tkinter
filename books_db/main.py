import tkinter as tk
import customtkinter as ctk

from db import DB


# Создаем объект класса DB
db = DB()

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")


class LibraryFrame(ctk.CTkFrame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        primary_color = "#B9F3FC"
        secondary_color = "slateblue"
        primary_font = 'monospace', 18

        self.configure(fg_color='transparent')

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        # Лейблы

        self.l1 = ctk.CTkLabel(self, text="Название",
                               text_color=primary_color, font=primary_font)

        self.l2 = ctk.CTkLabel(self, text="Автор",
                               text_color=primary_color, font=primary_font)

        self.l3 = ctk.CTkLabel(self, text="Год",
                               text_color=primary_color, font=primary_font)

        self.l1.grid(row=0, column=0, sticky='w', padx=20)
        self.l2.grid(row=0, column=3, sticky='w', padx=(0, 20))
        self.l3.grid(row=0, column=5, sticky='w', padx=(0, 20))

        # Поля для ввода

        self.title_text = ctk.StringVar()
        self.e1 = ctk.CTkEntry(self, textvariable=self.title_text)

        self.author_text = ctk.StringVar()
        self.e2 = ctk.CTkEntry(self, textvariable=self.author_text)

        self.year_text = ctk.StringVar()
        self.e3 = ctk.CTkEntry(self, textvariable=self.year_text)

        self.e1.grid(row=1, column=0, columnspan=3, sticky="we", padx=20)
        self.e2.grid(row=1, column=3, columnspan=2, sticky="we", padx=(0, 20))
        self.e3.grid(row=1, column=5, sticky="we", padx=(0, 20))

        # # LISTBOX

        self.list1 = tk.Listbox(self, borderwidth=0, bg=self['bg'], fg='white', font=('monospace, 12'))
        self.list1.grid(row=2, column=0, columnspan=6,
                             sticky='ew', padx=20, pady=20)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        # # Scrollbar
        self.my_scrollbar = ctk.CTkScrollbar(
            self, command=self.list1.yview)
        self.my_scrollbar.grid(row=2, column=6, sticky='nsw', pady=20)
        self.list1.configure(yscrollcommand=self.my_scrollbar.set)

        # BUTTONS

        self.b1 = ctk.CTkButton(self, text="Просмотр", command=self.view)
        self.b1.grid(row=3, column=0, sticky="we", padx=(20, 10))

        self.b2 = ctk.CTkButton(self, text="Поиск", command=self.search)
        self.b2.grid(row=3, column=1, sticky="we", padx=(0, 10))

        self.b3 = ctk.CTkButton(self, text="Добавить", command=self.add)
        self.b3.grid(row=3, column=2, sticky="we", padx=(0, 10))

        self.b4 = ctk.CTkButton(self, text="Обновить", command=self.update)
        self.b4.grid(row=3, column=3, sticky="we", padx=(0, 10))

        self.b5 = ctk.CTkButton(self, text="Удалить", command=self.delete_command)
        self.b5.grid(row=3, column=4, sticky="we", padx=(0, 10))

        self.b6 = ctk.CTkButton(self, text="Закрыть", command=container.destroy)
        self.b6.grid(row=3, column=5, sticky="we", padx=(0, 10))


        # Показываем таблицу
        self.view()

        



    def add(self):
        '''Добавить строку в таблицу'''
        db.insert(self.title_text.get(), self.author_text.get(), self.year_text.get())
        self.list1.delete(0, 'end')
        # self.list1.insert('end', (self.title_text.get(), self.author_text.get(), self.year_text.get()))
        self.view()
        
    def view(self):
        '''Вывод всех строк из базы данных'''
        self.list1.delete(0, 'end') 
        for row in db.view(): 
            self.list1.insert('end', row) 
        

    def get_selected_row(self, event): 
        '''Выбор строки из списка'''
        global selected_tuple
        index = self.list1.curselection()[0] #id выбранной строки
        # print(self.list1.curselection())
        selected_tuple = self.list1.get(index) 
        print(selected_tuple)
        self.e1.delete(0, 'end')                 
        self.e1.insert('end', selected_tuple[1]) 
        self.e2.delete(0, 'end')
        self.e2.insert('end', selected_tuple[2])
        self.e3.delete(0, 'end')
        self.e3.insert('end', selected_tuple[3]) 


    def search(self): 
        '''Поиск по автору или по названию'''
        self.list1.delete(0, 'end')   
        for row in db.search(self.title_text.get(), self.author_text.get()):
            self.list1.insert('end', row) 


    def update(self):
        '''Изменить строку'''
        db.update(selected_tuple[0], self.title_text.get(), self.author_text.get()) 


    def delete_command(self):
        '''Удалить строку'''
        db.delete(selected_tuple[0]) 
        self.view()



    


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('My Books')
        self.configure(padx=20, pady=20)
        self.minsize(600, 0)
        self.maxsize(800, 0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.library_frame = LibraryFrame(container=self)
        self.library_frame.grid(
            row=0, column=0, padx=20, pady=20, sticky="nsew")


        


if __name__ == "__main__":
    App().mainloop()
