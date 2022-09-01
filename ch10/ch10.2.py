from scratch.linear_algebra import Matrix, Vector, make_matrix
from scratch.statistics import correlation
from typing import List


def correlation_matrix(data: List[Vector]) -> Matrix:
    """
    Возвращает матрицу размера len(data) x len(data),
    (i, j)-й элемент которой является корреляцией между data[i] и data[j]
    :param data: входные данные
    :return: матрица корреляций
    """
    def correlation_ij(i: int, j: int) -> float:
        return correlation(data[i], data[j])

    return make_matrix(len(data), len(data), correlation_ij)
