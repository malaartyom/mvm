import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List


def f(x, y):
    return y


def f1(t, x, y):
    # a = 10
    # b = 2
    # return a * x - b * x * y
    return 10 * x - 2 * x * y


def f2(t, x, y):
    # c = 2
    # d = 10
    # return c * x * y - d * y
    return 2 * x * y - 10 * y


def lorenz(r, sigma=10, b=8 / 3):
    lf1 = lambda t, x, y, z: sigma * (y - x)
    lf2 = lambda t, x, y, z: x * (r - z) - y
    lf3 = lambda t, x, y, z: x * y - b * z
    return lf1, lf2, lf3


def get_grid(n: int, borders: Tuple[int, int]) -> List[int]:
    l, r = borders
    h = (r - l) / n
    return [l + i * h for i in range(n + 1)]


def rk_4(func, y_0, borders: Tuple[int, int], n: int) -> List[int]:
    l, r = borders
    h = (r - l) / n
    x = get_grid(n, borders)
    y = [y_0]
    for i in range(n):
        x_i = x[i]
        y_i = y[i]
        k1 = func(x_i, y_i)
        k2 = func(x_i + h / 2, y_i + h * k1 / 2)
        k3 = func(x_i + h / 2, y_i + h * k2 / 2)
        k4 = func(x_i + h, y_i + h * k3)
        y.append(y_i + ((h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)))
    return y


def rk_4_2d(func1, func2, x_0, y_0, borders: Tuple[int, int], n: int):
    l, r = borders
    h = (r - l) / n
    t = get_grid(n, borders)
    x = [x_0]
    y = [y_0]
    for i in range(n):
        t_i, x_i, y_i = t[i], x[i], y[i]
        k1 = func1(t_i, x_i, y_i) * h
        m1 = func2(t_i, x_i, y_i) * h
        k2 = func1(t_i + h / 2, x_i + k1 / 2, y_i + m1 / 2) * h
        m2 = func2(t_i + h / 2, x_i + k1 / 2, y_i + m1 / 2) * h
        k3 = func1(t_i + h / 2, x_i + k2 / 2, y_i + m2 / 2) * h
        m3 = func2(t_i + h / 2, x_i + k2 / 2, y_i + m2 / 2) * h
        k4 = func1(t_i + h, x_i + k3, y_i + m3) * h
        m4 = func2(t_i + h, x_i + k3, y_i + m3) * h

        x.append(x_i + ((1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)))
        y.append(y_i + ((1 / 6) * (m1 + 2 * m2 + 2 * m3 + m4)))
    return x, y


def rk_4_lorenz(func1, func2, func3, x_0, y_0, z_0, borders: Tuple[int, int], n: int):
    l, r = borders
    h = (r - l) / n
    t = get_grid(n, borders)
    x, y, z = [x_0], [y_0], [z_0]
    for i in range(n):
        t_i, x_i, y_i, z_i = t[i], x[i], y[i], z[i]
        k1 = func1(t_i, x_i, y_i, z_i) * h
        m1 = func2(t_i, x_i, y_i, z_i) * h
        q1 = func3(t_i, x_i, y_i, z_i) * h
        k2 = func1(t_i + h / 2, x_i + k1 / 2, y_i + m1 / 2, z_i + q1 / 2) * h
        m2 = func2(t_i + h / 2, x_i + k1 / 2, y_i + m1 / 2, z_i + q1 / 2) * h
        q2 = func3(t_i + h / 2, x_i + k1 / 2, y_i + m1 / 2, z_i + q1 / 2) * h
        k3 = func1(t_i + h / 2, x_i + k2 / 2, y_i + m2 / 2, z_i + q2 / 2) * h
        m3 = func2(t_i + h / 2, x_i + k2 / 2, y_i + m2 / 2, z_i + q2 / 2) * h
        q3 = func3(t_i + h / 2, x_i + k2 / 2, y_i + m2 / 2, z_i + q2 / 2) * h
        k4 = func1(t_i + h, x_i + k3, y_i + m3, z_i + q3) * h
        m4 = func2(t_i + h, x_i + k3, y_i + m3, z_i + q3) * h
        q4 = func3(t_i + h, x_i + k3, y_i + m3, z_i + q3) * h

        x.append(x_i + ((1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)))
        y.append(y_i + ((1 / 6) * (m1 + 2 * m2 + 2 * m3 + m4)))
        z.append(z_i + ((1 / 6) * (q1 + 2 * q2 + 2 * q3 + q4)))
    return x, y, z


def show_rk_4() -> None:
    y_0 = 1
    n = 10000
    borders = (-10, 10)
    t = get_grid(n, borders)
    show_simple_rk_4(n, y_0)
    show_predator_victim(borders, n, t)
    show_lorenz(borders, n)

    plt.show()


def show_lorenz(borders, n):
    fig = plt.figure("3")
    ax = fig.add_subplot(111, projection='3d')
    x0, y0, z0 = 1, 1, 1
    r = 100
    lf1, lf2, lf3 = lorenz(r)
    lor = rk_4_lorenz(lf1, lf2, lf3, x0, y0, z0, borders, n)
    ax.plot(lor[0], lor[1], lor[2])
    # for r in np.linspace(10, 24, 3):
    #     lf1, lf2, lf3 = lorenz(r)
    #     lor = rk_4_lorenz(lf1, lf2, lf3, x0, y0, z0, borders, n)
    #     ax.scatter(lor[0], lor[1], lor[2], s=2)


def show_predator_victim(borders, n, t):
    # x0 = 1
    # y0 = 1
    # rk_2d = rk_4_2d(f1, f2, x0, y0, borders, n)
    fig = plt.figure("2")
    # ax = fig.add_subplot(111, projection='3d')
    for x in np.linspace(0.2, 2, 3):
        for y in np.linspace(0.2, 2, 3):
            rk_2d = rk_4_2d(f1, f2, x, y, borders, n)
            if not (any(np.isnan(i) or np.isinf(i) for i in rk_2d[0])) and not (
                    any(np.isnan(i) or np.isinf(i) for i in rk_2d[1])):
                plt.plot(rk_2d[0], rk_2d[1])


def show_simple_rk_4(n, y_0):
    borders = (0, 2)
    t = get_grid(n, borders)
    rk = rk_4(f, y_0, borders, n)
    exp = [np.exp(i) for i in t]
    diff = [rk[i] - exp[i] for i in range(len(t))]
    plt.figure("1")
    plt.suptitle(u'{} \u2044 {}'.format('dy', "dx") + " = y \n y0 = 1", color="red")
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.subplot(1, 2, 1)
    plt.xlabel("Ось X")
    plt.ylabel("Ось Y")
    plt.plot(t, rk, label="Рунге-Кутта")
    plt.plot(t, exp, label="Экспонента")
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(t, diff, label="Разность")
    plt.legend()


if __name__ == "__main__":
    show_rk_4()
