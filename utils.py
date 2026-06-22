"""
Вспомогательные функции для симуляции.
"""

import random


def random_energy(min_val: float = 0.0, max_val: float = 100.0) -> float:
    """
    Возвращает случайное значение энергии.

    :param min_val: минимальное значение
    :param max_val: максимальное значение
    :return: случайное число с одним знаком после запятой
    """
    return round(random.uniform(min_val, max_val), 1)
