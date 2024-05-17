from collections.abc import Callable
from typing import Tuple, List
from tqdm import tqdm
from fifth_task import Tridiagonal
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
    true_x = [x_0 / np.linalg.norm(x_0)]
    y_k, eigen_value = None, None
    for i in tqdm(range(n)):
        # y = np.linalg.inv(A) @ x[i]
        y = list(np.linalg.solve(A, true_x[i])) # это я ситаю, чтобы сравнивать с y_k. Если посмотреть глазами, то они не сильно отличаются
        # print(f"x{i} = {x[i]}")
        y_k = solve(A, x[i])
        # print(np.linalg.norm(y_k) ** 2)
        # print(f"y_{i} = {y_k}")
        eigen_value = (x[i] @ y_k) / (np.linalg.norm(y_k) ** 2)
        e.append((true_x[i] @ y) / (np.linalg.norm(y) ** 2)) # правильные с.з хранятся тут

        x_i = y_k / np.linalg.norm(y_k)
        x_i[0] = 0
        x_i[-1] = 0

        true_x_i = y / np.linalg.norm(y) # "настоящие" значения x[i] хранятся тут и вот они уже значительно отличаются от x_i
        true_x_i[0] = 0
        true_x_i[-1] = 0

        x.append(x_i)
        true_x.append(true_x_i)
    # print(x[-1])
    print(f"e = {eigen_value}")
    # print(e[-1])

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

print("Энергия на промежутке (-1000, 1000)", solution0[1])
print("Настоящее значение энергии", min(np.linalg.eigvals(H0))) # а тут всё сходится  :)


plt.style.use('seaborn-v0_8-whitegrid')
plt.subplot(1, 2, 1)
plt.plot(grid, solution[0])
plt.subplot(1, 2, 2)
plt.plot(grid0, solution0[0])
plt.show()
