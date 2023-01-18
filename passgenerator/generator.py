import random

def generate(number_of_symbols=12):

    symbols = []
    for i in range(number_of_symbols):
        num = random.randint(1, 4)
        if num == 1:
            symbols.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        elif num == 2:
            symbols.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        elif num == 3:
            symbols.append(random.choice('0123456789'))
        elif num == 4:
            symbols.append(random.choice('!@#$%^&*<>?'))

    password = ''.join(str(symb) for symb in symbols)
    return password



if __name__ == "__main__":
    print(generate(12))
