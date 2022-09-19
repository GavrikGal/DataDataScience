from typing import Tuple
from scratch.linear_algebra import Vector
from scratch.statistics import correlation, standard_deviation, mean, de_mean
from scratch.statistics import num_friends_good, daily_minutes_good


def predict(alpha: float, beta: float, x_i: float) -> float:
    return beta * x_i + alpha


def error(alpha: float, beta: float, x_i: float, y_i: float) -> float:
    """Ошибка предсказания beta * x_i + alpha,
    когда фактическое значение равно y_i"""
    return predict(alpha, beta, x_i) - y_i


def sum_of_sqerrors(alpha: float, beta: float, x: Vector, y: Vector) -> float:
    return sum(error(alpha, beta, x_i, y_i) ** 2
               for x_i, y_i in zip(x, y))


def least_squares_fit(x: Vector, y: Vector) -> Tuple[float, float]:
    """Учитывая векторы x и y, отыскать
    значение alpha и beta по наименьшим квадратам"""
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta


x = [i for i in range(-100, 100, 10)]
y = [3 * i - 5 for i in x]

# Должна отыскать, что y = 3x - 5
assert least_squares_fit(x, y) == (-5, 3)

alpha, beta = least_squares_fit(num_friends_good, daily_minutes_good)

assert 22.9 < alpha < 23.0
assert 0.9 < beta < 0.905


def total_sum_of_squares(y: Vector) -> float:
    """полная сумма квадратов отклонений y_i от их среднего"""
    return sum(v ** 2 for v in de_mean(y))


def r_squared(alpha: float, beta: float, x: Vector, y: Vector) -> float:
    """Доля отклонения в y, улавливаемая моделью, которая равна
    '1 - доля отклонения в y, не улавливаемая моделью'"""
    return 1.0 - (sum_of_sqerrors(alpha, beta, x, y) /
                  total_sum_of_squares(y))


rsq = r_squared(alpha, beta, num_friends_good, daily_minutes_good)
assert 0.328 < rsq < 0.330
