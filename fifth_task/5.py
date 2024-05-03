import numpy as np
import math
import matplotlib.pyplot as plt


def answer(x, df_left, f_right):
    return -np.cos(x) + (df_left + 1) * x + f_right - ((df_left + 1) * np.pi) / 2


def get_right_part(func, n: int, l: float, r: float):
    h = (r - l) / n
    return [func(l + i * h) for i in range(1, n)]


def get_roots(n: int, l: float, r: float):
    h = (r - l) / (n)
    return [l + i * h for i in range(n + 1)]


def border_cond_0(f_right, df_left, h):
    left_border_cond = [-1 / h, 1 / h, df_left]
    right_border_cond = [0, 1, f_right]
    return left_border_cond, right_border_cond


def border_cond_1(f_left, f_right):
    left_border_cond = [1, 0, f_left]
    right_border_cond = [0, 1, f_right]
    return left_border_cond, right_border_cond


def create_matrix(func, n: int, l: float, r: float, f_right=0, df_left=0, f_left=0, df_right=0):
    if n < 3:
        raise IndexError("Matrix can't have shape less then 3")
    h = (r - l) / n
    left_border_cond, right_border_cond = border_cond_0(f_right, df_left, h)

    a, b, c, right_part = [0], [], [], []

    b.append(left_border_cond[0])
    c.append(left_border_cond[1])
    right_part.append(left_border_cond[2])
    right_part.extend(get_right_part(func, n, l, r))

    for i in range(1, n):
        a.append(1 / (h ** 2))
        b.append(-2 / (h ** 2))
        c.append(1 / (h ** 2))
    c.append(0)

    a.append(right_border_cond[0])
    b.append(right_border_cond[1])
    right_part.append(right_border_cond[2])

    return a, b, c, right_part


def tridiagonal_matrix_algorithm(a, b, c, right_part):
    for i in range(len(a) - 1):
        b_i, c_i, right_part_i = b[i], c[i], right_part[i]
        right_part[i + 1] = right_part[i + 1] - (right_part_i / b_i) * a[i + 1]
        b[i + 1] = b[i + 1] - (a[i + 1] / b_i) * c_i

    b[len(a) - 1] = right_part[len(a) - 1] / b[len(a) - 1]

    for i in range(len(a) - 2, -1, -1):
        b[i] = (right_part[i] - c[i] * b[i + 1]) / b[i]

    return b


if __name__ == "__main__":
    f_right = 100
    df_left = -100
    a, b, c, right_part = create_matrix(math.cos, 4, -np.pi / 2, np.pi / 2, f_right=f_right, df_left=df_left)
    print("a =", a)
    print("b = ", b)
    print("c = ", c)
    print("right part = ", right_part)
    result = tridiagonal_matrix_algorithm(a, b, c, right_part)
    print(result)

    x = get_roots(4, -np.pi / 2, np.pi / 2)
    answ = [answer(i, df_left, f_right) for i in x]
    diff = [result[r] - answ[r] for r in range(len(result))]
    print(x)
    print(result)
    print(answ)
    print(diff)

    plt.plot(x, answ, label = "Точное решение")
    plt.plot(x, result, label="Численное решение решение")
    plt.plot(x, diff, label = "Разность")
    plt.legend()
    plt.show()
