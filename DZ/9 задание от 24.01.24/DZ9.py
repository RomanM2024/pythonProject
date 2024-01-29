a = int(input("Введите элементы кортежа: "))
a = str(a)
print(tuple(a))
for i in set(a):
    print("Количество", i, "=", a.count(i))
