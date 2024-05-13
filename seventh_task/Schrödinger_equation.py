from collections.abc import Callable
from typing import Tuple, List
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np


def get_grid(n: int, borders: Tuple[int, int]) -> List[int]:
    l, r = borders
    h = (r - l) / n
    return [l + i * h for i in range(n)]


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
    # Задание граничных условий
    H[0, 0] = 1
    H[0, 1] = 0
    H[-1, n - 2] = 0
    H[-1, n - 1] = 1

    return H


def inverse_power_method(n: int, A: np.matrix):
    x_0 = np.ones(n)
    # Это тоже задание граничных условий
    x_0[0] = -1
    x_0[-1] = 1

    x = [x_0 / np.linalg.norm(x_0)]
    y_k, eigen_value = None, None
    for i in tqdm(range(n)):
        # y_k = np.linalg.inv(A) @ x[i]
        y_k = np.linalg.solve(A, x[i])
        eigen_value = (x[i] @ y_k) / (np.linalg.norm(y_k) ** 2)
        x.append(y_k / np.linalg.norm(y_k))
    return y_k, eigen_value




U = lambda x: x ** 2
n = 100
borders = (0, 4)
grid = get_grid(n, borders)
H = create_hamilton_matrix(U, n, borders)
# print(H)
solution = inverse_power_method(n, H)
print("Волновая функция:", solution[0])
print("Энергия", solution[1])
print("Минимальное собственное значения H (с помощью numpy):", min(np.linalg.eigvals(H)))
plt.style.use('seaborn-v0_8-whitegrid')
plt.plot(grid, solution[0])
plt.show()



