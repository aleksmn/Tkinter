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

    user_input = text_entry.get()

    text = tk.Label(output_frame, text=user_input)
    text.config(bg=text.master['bg'])

    text.pack()

    text_entry.delete(0, 'end')


def count_up(number):
    '''Count up on the app'''
    global value

    text = tk.Label(output_frame, text=number)
    text.config(bg=text.master['bg'])
    text.pack()

    value = number + 1


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

print_button.grid(row=0, column=1, padx=(0,10), ipadx=30, pady=10)


# Output
output_frame.pack_propagate(0)


# Pass a parameter

value = 0
count_button = tk.Button(input_frame, text='Count', command=lambda:count_up(value))
count_button.grid(row=1, column=0, columnspan=2, padx=10, ipadx=30, pady=5, sticky='we')


# Запускаем основной цикл программы
root.mainloop()
