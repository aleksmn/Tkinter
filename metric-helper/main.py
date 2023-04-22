# Metric Helper
import customtkinter as ctk

# Настраиваем тему
ctk.set_appearance_mode("light")

# Создаем окно
root = ctk.CTk()
root.title('Metric Helper')
root.resizable(0, 0)

# Определяем цвета и шрифт
field_font = ('sans-serif', 14)

primary_color = "purple"
secondary_color = "slateblue"


# Функции

def convert():
    """Переводим одну величину в другую"""

    print('Конвертируем')

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
    output_field.insert(0, str(end_value))




# Определяем разметку окна

# Создаем поля ввода и вывода

input_field = ctk.CTkEntry(
    root, width=190, font=field_font, placeholder_text="Enter value")

output_field = ctk.CTkEntry(root, width=190, font=field_font)

equal_label = ctk.CTkLabel(root, text="=", font=field_font)


input_field.grid(row=0, column=0, padx=10, pady=10)
equal_label.grid(row=0, column=1, padx=10, pady=10)
output_field.grid(row=0, column=2, padx=10, pady=10)


# Комбобокс
metric_list = ['femto', 'pico', 'nano', 'micro', 'milli', 'centi', 'deci',
               'base value', 'deca', 'hecto', 'kilo', 'mega', 'giga', 'tera', 'peta']


input_combobox = ctk.CTkComboBox(
    root, width=190, values=metric_list, font=field_font, justify='left', button_color=secondary_color)



output_combobox = ctk.CTkComboBox(
    root, width=190, values=metric_list, font=field_font, justify='left', button_color=secondary_color)


to_label = ctk.CTkLabel(root, text="to", font=field_font)


input_combobox.grid(row=1, column=0, padx=10, pady=10)
to_label.grid(row=1, column=1, padx=10, pady=10)
output_combobox.grid(row=1, column=2, padx=10, pady=10)


input_combobox.set('base value')
output_combobox.set('base value')



# Кнопка перевода величин
convert_button = ctk.CTkButton(root, 
                                text='Convert', 
                                font=field_font, 
                                fg_color=primary_color, 
                                hover_color=secondary_color,
                                command=convert)


convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)


# Запуск основного цикла
root.mainloop()
