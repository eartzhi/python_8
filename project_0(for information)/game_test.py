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
    predict_list = [x for x in range(0, predict_range+1)]
    predict_num = len(predict_list)//2
    # predict используем просто для информации о перебираемом числе
    predict = predict_list[predict_num]
    count = 1
    
    # За один проход убираем половину неподходящих чисел
    while predict != number:
        count += 1
        if predict_list[predict_num] < number:
            predict_list = predict_list[len(predict_list)//2:]
            predict_num = len(predict_list)//2
            predict = predict_list[predict_num]
        elif predict_list[predict_num] > number:
            predict_list = predict_list[:len(predict_list)//2]
            predict_num = len(predict_list)//2
            predict = predict_list[predict_num]
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
