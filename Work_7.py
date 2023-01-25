# Задание 7. Программа 'Таможня'

name = ''
register_list = {}
print('Вас приветствует программа таможенного контроля!. \nДля завершения программы введите слово "end"\n')
while name != 'end':
    name = input('Кто пересекает границу? Введите имя: ')
    if name == 'end':
        break
    elif name in register_list:
        register_list[name] += 1
    else:
        register_list[name] = 1
print('\nИмя - количество пересечений границы: ')
for key, value in register_list.items():
    print(f'{key} - {value}')
