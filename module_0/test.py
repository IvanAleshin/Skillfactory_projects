import numpy as np

limit_number = int(input('До какого числа можно загадать компьютеру?: '))  # нужно для определения возможного инетервала
number = np.random.randint(1, limit_number + 1)  # компьютер загадывает число
print(f"Загадано число в интервале от 1 до {limit_number}")


def game_core_v3(number):
    """В интервале возможных загаданных чисел функция проверяет число посередине. В зависимости от результата (< или >
    загаданного числа) меняем нижнюю или верхнюю границу предполагаемого интервала и уже в нём проверяем число
    посередине. При совпадении с загаданным числом функция выводит число попыток, за которое смогла вычислить число"""
    global limit_number
    max_number = limit
    count = 1  # счетчик попыток
    min_number = 1  # какое минимальное число мог загадать компьютер
    predict = int((max_number + 1 - min_number) / 2)  # предполагаемое число
    while predict != number:
        if predict > number:
            count += 1
            max_number = predict
            predict = int((max_number - min_number) / 2) + min_number
        else:
            count += 1
            min_number = predict
            predict = int((max_number + 1 - min_number) / 2) + min_number
    return count


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v3)

print(f'Загадано число {number}')