# Дана строка в формате 1:02:15
# часы или минуты могут отсутсвовать
# нужно из этой строки извлечь часы, минуты и секунды

# string = "12:02:15"

# hours =
# minutes =
# seconds =


time_entry = input("Введите время: ")

hours, minutes, seconds = 0, 0, 0

# Получаем список, например ['12', '02', '15']
string_split =  time_entry.split(":")

if len(string_split) == 3:
    hours = int(string_split[0])
    minutes = int(string_split[1])
    seconds = int(string_split[2])
elif len(string_split) == 2:
    minutes = int(string_split[0])
    seconds = int(string_split[1])
elif len(string_split) == 1:
    seconds = int(string_split[0])
else:
    print("Неверный формат ввода")


# Проверка
print('Часы:', hours)
print('Минуты:', minutes)
print('Секунды:', seconds)



# Посчитать, сколько это секунд:

full_seconds = hours * 3600 + minutes * 60 + seconds

print("Общее кол-во секунд:", full_seconds)






# divmod


# divmod(9, 5)  
#---> (1, 4)