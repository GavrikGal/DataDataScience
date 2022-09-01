from typing import Callable, List


Matrix = List[List[float]]


def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """Возвращает матрицу размера num_rows x num_cols,
    чей (i,j)-й элемент являеется функцией entry_fn(i, j)
    """
    return [[entry_fn(i, j)
             for j in range(num_cols)]
            for i in range(num_rows)]