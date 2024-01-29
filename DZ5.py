s = []
n = int(input("Введите кол-во элементов списка: "))
for num in range(n):
    x = int(input("Введите число кратное 3: "))
    if x % 3 == 0:
        s.append(x)
    else:
        print(x, "не делится на 3 без остатка")
print(s)






