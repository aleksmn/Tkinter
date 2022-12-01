# Functions

import tkinter as tk


# Создаем окно программы
root = tk.Tk()
root.title("Функции")
root.iconphoto(True, tk.PhotoImage(file='logo.png'))
root.geometry('500x500')
root.resizable(0, 0)
root.config(bg='#10A19D')

# Functions

def make_label():
    '''Print a label to the app'''
    # print('Hello world')

    text = tk.Label(output_frame, text=text_entry.get())
    text.config(bg=text.master['bg'])
    text.pack()

    text_entry.delete(0, 'end')







# Фреймы
input_frame = tk.Frame(root, bg='orange', width=500, height=100)
output_frame = tk.Frame(root, bg='lightblue', width=500, height=400)

input_frame.pack(padx=10, pady=10)
output_frame.pack(padx=10, pady=(0, 10))


# Inputs

text_entry = tk.Entry(input_frame, width=40)
text_entry.grid(row=0, column=0, padx=10, pady=5, ipady=4)
input_frame.grid_propagate(0)


print_button = tk.Button(input_frame, text="Print!", command=make_label)

print_button.grid(row=0, column=1, ipadx=30, pady=20)


# Output
output_frame.pack_propagate(0)


# Pass a parameter



# Запускаем основной цикл программы
root.mainloop()
