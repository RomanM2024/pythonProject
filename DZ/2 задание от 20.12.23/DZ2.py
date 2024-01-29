print("Введите количество копеек: ")
def funcion(num):
    if num % 10 == 1 and num % 100 != 11:
        return f'{num} копейка'
    elif num % 10 in [2, 3, 4] and num % 100 not in [12, 13, 14]:
        return f'{num} копейки'
    else:
        return f'{num} копеек'

print(funcion(int(input())))







