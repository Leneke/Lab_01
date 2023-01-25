# Задание 3. Дано одно число Price - цена на 1 кг апельсин. Вывести стоимость 1, 2, ..., 10 кг апельсин.
# (Попытайтесь решить задачу двумя способами: циклом FOR и циклом WHILE)

# price = 550
# check = 0
# for i in range(11):
#     check = price * i
#     print(check)
#
price = 550
i = 0
while i<10:
    i += 1
    check = price * i
    print(check)
