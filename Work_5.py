# Задание 5. Напишите программу "Угадай число".

from random import randint

print('Добро пожаловать в игру "Угадай число"')
name = input('Введите ваше имя: ')
print(f'Привет, {name}! Давайте сыграем. Угадайте число от 1 до 10. У вас три попытки.')
choice = ''
while choice != 'н':

    secret = randint(1, 10)
    life = 3

    while life != 0:
        life -= 1

        try:
            number = int(input('Введите число: '))

            if number == secret:
                print(f'Поздравляю, {name}! Вы угадали! ;-)')
                break
            elif number < 1 or number > 10:
                print(f'Вы ошиблись, {number} не подходит. Загадано число от 1 до 10')
            elif number < secret:
                print(f'Не правильно. Загаданное число больше {number}')
            else:
                number > secret
                print(f'Не правильно. Загаданное число меньше {number}')
        except ValueError:
            print('Это не число')

        if life > 0:
            print(f'Количество оставшихся попыток: {life}\n')
        if life == 0:
            print(f'Ой, попытки закончились! :-( \nЧто будем делать, {name}?')

    print('Сыграем еще раз?\n')
    choice = input(f'Нажмите "д", если хотите повторить или "н", чтобы закончить игру: ').lower()

    while choice != 'д' and choice != 'н':
        print('Ваш ответ не распознан, повторите')
        choice = input(f'Нажмите "д", если хотите повторить или "н", чтобы закончить игру ').lower()

    if choice == 'д':
        print('\nОтлично, играем снова!.\nУгадайте число от 1 до 10. У вас три попытки.')
    if choice == 'н':
        print(f'Игра окончена. До свидания, {name}!')

