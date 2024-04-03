"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def predict(number: int = 1, predict_range: int = 100) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        predict_range (int, optional): Диапазон загадонного числа. Defaults to 100.

    Returns:
        int: Число попыток
    """
    # Создаем список чисел, чтобы было удобнее оперировать
    predict = predict_range//2
    predict_range_min = 0
    predict_range_max = predict_range
    count = 1
    
    # За один проход убираем половину неподходящих чисел
    while predict != number:
        count += 1
        if predict < number:
            predict_range_min = predict
            predict = (predict_range_max+predict_range_min) // 2
            
        elif predict > number:
            predict_range_max = predict
            predict = (predict_range_max+predict_range_min) // 2
            
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

if __name__ == "__main__":
    # RUN
    score_game(predict)
