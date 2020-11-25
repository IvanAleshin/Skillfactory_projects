import numpy as np
from math import ceil

count = 0  # счетчик попыток
max_chislo = int(input('До какого числа можно загадать компьютеру?: '))
min_chislo = 1  # какое минимальное число мог загадать компьютер
number = np.random.randint(1, max_chislo + 1)  # компьютер загадывает число
print(f"Загадано число в интервале от 1 до {max_chislo}")

chislo = ceil((max_chislo + 1 - min_chislo) / 2)  # выбираем число посередине интервала
print(chislo)

while chislo != number:
    count += 1
    if chislo > number:
        max_chislo = chislo
        chislo = ceil((max_chislo - min_chislo) / 2) + min_chislo
    else:
        min_chislo = chislo
        chislo = ceil((max_chislo - min_chislo) / 2) + min_chislo

print(f'Число {number} угадано с {count} попытки')

"""def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно
     или меньше нужного. Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    global min_chislo
    global max_chislo
    global interval
    predict = ceil((max_chislo - min_chislo + 1) / 2)
    while number != predict:
        count += 1
        if number > predict:
            min_chislo = predict
            predict = ceil((max_chislo - min_chislo + 1) / 2)
        elif number < predict:
            max_chislo = predict
            predict = ceil((max_chislo - min_chislo + 1) / 2)
    return(count) # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

game_core_v3(number)"""
