from collections.abc import Callable
from typing import Tuple, List
from tqdm import tqdm
from fifth_task import Tridiagonal
import matplotlib.pyplot as plt
import numpy as np

import numpy as np

def tridiagonal_matrix_algorithm(a, b, c, d):
  """Решает систему уравнений с трехдиагональной матрицей с помощью метода прогонки.

  Args:
    a: Нижняя диагональ матрицы.
    b: Главная диагональ матрицы.
    c: Верхняя диагональ матрицы.
    d: Правая часть системы уравнений.

  Returns:
    Список значений x, удовлетворяющих системе уравнений.
  """

  n = len(a)
  x = np.zeros(n)

  # Прямой ход
  for i in range(1, n):
    m = a[i] / b[i - 1]
    b[i] = b[i] - m * c[i - 1]
    d[i] = d[i] - m * d[i - 1]

  # Обратный ход
  x[n - 1] = d[n - 1] / b[n - 1]
  for i in range(n - 2, -1, -1):
    x[i] = (d[i] - c[i] * x[i + 1]) / b[i]

  return x


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


def solve(A: np.matrix, x):
    diagonals = A.diagonal().tolist()

    above_diagonals = []
    for i in range(A.shape[0] - 1):
        above_diagonals.append(A[i, i + 1])

    below_diagonals = []
    for i in range(1, A.shape[1]):
        below_diagonals.append(A[i, i - 1])

    # print(diagonals, above_diagonals, below_diagonals)
    # print(x)
    return Tridiagonal.tridiagonal_matrix_algorithm(below_diagonals, diagonals, above_diagonals, x)
    # return tridiagonal_matrix_algorithm(below_diagonals, diagonals, above_diagonals, x)


def inverse_power_method(n: int, A: np.matrix):
    x_0 = np.ones(n)
    # Это тоже задание граничных условий
    x_0[0] = 0
    x_0[-1] = 0
    e = []
    x = [x_0 / np.linalg.norm(x_0)]
    y_k, eigen_value = None, None
    for i in tqdm(range(n)):
        # y_k = np.linalg.inv(A) @ x[i]
        y = list(np.linalg.solve(A, x[i]))
        # print(f"x{i} = {x[i]}")
        y_k = solve(A, x[i])
        # print(np.linalg.norm(y_k) ** 2)
        # print(f"y_{i} = {y_k}")
        eigen_value = (x[i] @ y_k) / (np.linalg.norm(y_k) ** 2)
        e.append((x[i] @ y) / (np.linalg.norm(y) ** 2))
        x_i = y_k / np.linalg.norm(y_k)
        x_i[0] = 0
        x_i[-1] = 0
        x.append(x_i)
    # print(x[-1])
    print(f"e = {eigen_value}")
    print(e[-1])

    return y_k, eigen_value, e


U = lambda x: x ** 2
n = 100
borders = (-4, 4)
borders0 = (-1000, 1000)
grid = get_grid(n, borders)
grid0 = get_grid(n, borders0)
H = create_hamilton_matrix(U, n, borders)
# print(H)
H0 = create_hamilton_matrix(U, n, borders0)
# print(H)
solution = inverse_power_method(n, H)
solution0 = inverse_power_method(n, H0)
print("Собсвтенное значение, полученное методом прогонки", solution[1])
print("Собственное значение, получание с помощью np.solve()", solution[2][-1])

print("Волновая функция:", solution[0])
print("Энергия", solution[1])
print("Минимальное собственное значения H (с помощью numpy):", min(np.linalg.eigvals(H)))
plt.style.use('seaborn-v0_8-whitegrid')
plt.subplot(1, 2, 1)
plt.plot(grid, solution[0])
plt.subplot(1, 2, 2)
plt.plot(grid0, solution0[0])
plt.show()
