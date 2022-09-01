from typing import List, Dict
from collections import Counter
import math
import matplotlib.pyplot as plt


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
    plt.bar(list(histogram.key()),
            list(histogram.values()), width=bucket_size)
    plt.title(title)
    plt.show()

import random
from scratch.probability import inverse_normal_cdf


