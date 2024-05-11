from collections.abc import Callable
from typing import Tuple, List
from tqdm import tqdm

import numpy as np


def get_grid(n: int, borders: Tuple[int, int]) -> List[int]:
    l, r = borders
    h = (r - l) / n
    return [l + i * h for i in range(n + 1)]


def create_hamilton_matrix(U: Callable, n: int, borders: Tuple[int, int]) -> np.matrix:
    a, b = borders
    H = np.zeros((n, n))
    h = (b - a) / n
    x = get_grid(n, borders)
    for i in range(n):
        if i != n - 1:
            H[i + 1, i] = -1 / (2 * h ** 2)
        H[i, i] = (1 / (h ** 2)) + U(x[i])
        if i != 0:
            H[i - 1, i] = - 1 / (2 * h ** 2)
    return H


def inverse_power_method(n: int, A: np.matrix):
    x_0 = np.ones(n)
    x = [x_0 / np.linalg.norm(x_0)]
    y_k, eigen_value = None, None
    for i in tqdm(range(n)):
        y_k = np.linalg.inv(A) @ x[i]
        eigen_value = (x[i] @ y_k) / (np.linalg.norm(y_k) ** 2)
        x.append(y_k / np.linalg.norm(y_k))
    return y_k, eigen_value


U = lambda x: x ** 2
H = create_hamilton_matrix(U, 100, (0, 1))
solution = inverse_power_method(100, H)
print("Волновая функция:", solution[0])
print("Энергия", solution[1])
print("Минимальное собственное значения H (с помощью numpy):", min(np.linalg.eigvals(H)))


