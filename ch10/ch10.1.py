from typing import List, Dict
from collections import Counter
import math
import matplotlib.pyplot as plt
import random
from scratch.probability import inverse_normal_cdf
from scratch.statistics import correlation


def bucketize(point: float, bucket_size: float) -> float:
    """Округлить точку до следующего наименьшего кратного
    размера интервала bucket_size"""
    return bucket_size * math.floor(point / bucket_size)


def make_histogram(points: List[float], bucket_size: float) -> Dict[float, int]:
    """Разбивает точки на интервалы и подсчитывает
    их количество в каждом интервале"""
    return Counter(bucketize(point, bucket_size) for point in points)


def plot_histogram(points: List[float], bucket_size: float, title: str = ""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(list(histogram.keys()),
            list(histogram.values()), width=bucket_size)
    plt.title(title)
    plt.show()


random.seed(0)

# Равномерное распределение между -100 и 100
uniform = [200 * random.random() - 100 for _ in range(10000)]

# Нормальное распределение со средним 0, страндартным отклонением 57
normal = [57 * inverse_normal_cdf(random.random())
          for _ in range(10000)]

plot_histogram(uniform, 10, "Равномерная гистограмма")
plot_histogram(normal, 10, "Нормальная гистограмма")


def random_normal():
    """Возвращает случайную выборку из стандортнго нормального распределения"""
    return inverse_normal_cdf(random.random())


xs = [random_normal() for _ in range(1000)]
ys1 = [x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]

plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
plt.scatter(xs, ys2, marker='.', color='gray', label='ys2')
plt.xlabel('xs')
plt.ylabel('ys')
plt.legend(loc=9)
plt.title("Совсем разные совместные распределения")
plt.show()

print(correlation(xs, ys1))
print(correlation(xs, ys2))

