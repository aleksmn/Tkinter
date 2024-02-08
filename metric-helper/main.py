import ttkbootstrap as ttk
# tkinter


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
    output_field.configure(state="")
    output_field.delete(0, 'end')
    output_field.configure(state="readonly")

    # Получаем информацию от пользователя

    try:
        start_value = float(input_field.get())

    except:
        print('Неверный ввод')
        return

    start_prefix = input_combobox.get()
    end_prefix = output_combobox.get()

    print(start_value, start_prefix, end_prefix)

    # Переводим в основную величину, без префикса (граммы, метры)
    base_value = start_value * metric_values[start_prefix]

    # Переводим в новую величину
    end_value = base_value / metric_values[end_prefix]

    # Обновляем вывод
    output_field.configure(state="")
    output_field.insert(0, str(end_value))
    output_field.configure(state="readonly")



# Создаем окно
root = ttk.Window(
        title="Metric Helper",
        themename="cyborg", 
        resizable=(False, False)
    )

root.configure(padx=20, pady=20)

# Создаем поля ввода и вывода
input_field = ttk.Entry(root, style="primary")

output_field = ttk.Entry(root, state="readonly")

equal_label = ttk.Label(root, text="=")


input_field.grid(row=0, column=0, padx=10, pady=10, sticky="we")
equal_label.grid(row=0, column=1, padx=10, pady=10)
output_field.grid(row=0, column=2, padx=10, pady=10,  sticky="we")

# Комбобокс
metric_list = ['femto', 'pico', 'nano', 'micro', 'milli', 'centi', 'deci',
               'base value', 'deca', 'hecto', 'kilo', 'mega', 'giga', 'tera', 'peta']


input_combobox = ttk.Combobox(root, values=metric_list)

output_combobox = ttk.Combobox(root, values=metric_list)

to_label = ttk.Label(root, text="to")


input_combobox.grid(row=1, column=0, padx=10, pady=10)
to_label.grid(row=1, column=1, padx=10, pady=10)
output_combobox.grid(row=1, column=2, padx=10, pady=10)


input_combobox.set('base value')
output_combobox.set('base value')


# Кнопка перевода величин
convert_button = ttk.Button(root,
                               text='Convert',
                               command=convert)


convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)


# Запуск основного цикла
root.mainloop()