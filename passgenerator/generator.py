import random
import string

def generate_password(number_of_symbols=12):
    password = ''
    for i in range(number_of_symbols):
        randnum = random.randint(1, 4)

        if randnum == 1:
            password += random.choice(string.ascii_uppercase)
        elif randnum == 2:
            password += random.choice(string.ascii_lowercase)
        elif randnum == 3:
            password +=  random.choice(string.digits)
        else:
            password += random.choice("!@$#^&*-=?")

    return password



if __name__ == "__main__":
    print('Запущен модуль')
    print(generate_password(24))













# def generate_password(number_of_symbols=12):

#     symbols = []
#     for i in range(number_of_symbols):
#         num = random.randint(1, 4)
#         if num == 1:
#             symbols.append(random.choice(string.ascii_lowercase))
#         elif num == 2:
#             symbols.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
#         elif num == 3:
#             symbols.append(random.choice('0123456789'))
#         elif num == 4:
#             symbols.append(random.choice('!@#$%^&*<>?'))

#     password = ''.join(str(symb) for symb in symbols)
#     return password



# print(generate_password())









# if __name__ == "__main__":
#     print(generate_password(12))
