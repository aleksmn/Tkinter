# Metric Helper
import tkinter
from tkinter import ttk

# Создаем окно
root = tkinter.Tk()
root.title('Metric Helper')
root.iconphoto(True, tkinter.PhotoImage(file='logo.png'))
root.resizable(0, 0)

# Определяем цвета и шрифт
field_font = ('Cambria', 10)
bg_color = "#c75c5c"
button_color = "#f5cf87"
root.config(bg=bg_color)

# Функции

def convert():
    """Переводим одну величину в другую"""
    metric_values = {
        'femto': 10**-15,
        'pico': 10**-12,
        'nano': 10**-9,
        'micro': 10**-6,
        'milli': 10**-3,
        'centi': 10**-2,
        'deci': 10**-1,
        'base value': 10**0,
        'deca': 10**1,
        'hecto': 10**2,
        'kilo': 10**3,
        'mega': 10**6,
        'giga': 10**9,
        'tera': 10**12,
        'peta': 10**15
    }

    # Очищаем вывод
    output_field.delete(0, 'end')

    # Получаем информацию от пользователя
    start_value = float(input_field.get())
    start_prefix = input_combobox.get()
    end_prefix = output_combobox.get()

    # Переводим в основную величину, без префикса (граммы, метры)
    base_value = start_value*metric_values[start_prefix]

    # Переводим в новую величину
    end_value = base_value/metric_values[end_prefix]

    # Обновляем вывод
    output_field.insert(0, str(end_value))


# Определяем разметку окна

# Создаем поля ввода и вывода
input_field = tkinter.Entry(root, width=20, font=field_font, borderwidth=3)
output_field = tkinter.Entry(root, width=20, font=field_font, borderwidth=3)
equal_label = tkinter.Label(root, text="=>", font=field_font, bg=bg_color)
input_field.grid(row=0, column=0, padx=10, pady=10)
equal_label.grid(row=0, column=1, padx=10, pady=10)
output_field.grid(row=0, column=2, padx=10, pady=10)
# input_field.insert(0, 'Enter your quantity')

# Комбобокс
metric_list = ['femto', 'pico', 'nano', 'micro', 'milli', 'centi', 'deci',
               'base value', 'deca', 'hecto', 'kilo', 'mega', 'giga', 'tera', 'peta']
input_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify='center')
output_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify='center')

to_label = tkinter.Label(root, text="to", font=field_font, bg=bg_color)
input_combobox.grid(row=1, column=0, padx=10, pady=10)
to_label.grid(row=1, column=1, padx=10, pady=10)
output_combobox.grid(row=1, column=2, padx=10, pady=10)

input_combobox.set('base value')
output_combobox.set('base value')

# Кнопка перевода величин
convert_button = tkinter.Button(root, text='Convert', font=field_font, bg=button_color,
                                command=convert)
convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)

# Запуск основного цикла
root.mainloop()
