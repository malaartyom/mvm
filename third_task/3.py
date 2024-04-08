import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return 1 / (1 + 25 * x ** 2)


def get_roots(n):
    ans = []
    for i in range(n + 1):
        ans.append(((2 * i) / n) - 1)
    return ans


def get_chebishev_roots(n, a, b):
    ans = []
    for i in range(n + 1):
        ans.append(0.5 * (b + a) + 0.5 * (b - a) * np.cos(((2 * i + 1) * np.pi) / (2 * (n + 1))))
    return ans


def lagrange_polynomial_0(x, n):
    roots = get_roots(n)
    ans = 0
    for i, root in enumerate(roots):
        ans += (func(root) * w(x, i, roots)) / (dw(root, i, roots))
    return ans


def lagrange_polynomial_1(x, n, a, b):
    roots = get_chebishev_roots(n, a, b)
    answ = 0
    for i, root in enumerate(roots):
        answ += (func(root) * w(x, i, roots)) / (dw(root, i, roots))
    return answ


def w(x, i, roots):
    answ = 1
    for j, root in enumerate(roots):
        if i != j:
            answ *= (x - root)
    return answ


def dw(x_i, i, roots):
    answ = 1
    for j, root in enumerate(roots):
        if j != i:
            answ *= (x_i - root)
    return answ


def count_approx():
    approx = []
    chebishev_approx = []
    for n in range(2, 11):
        approx.append(max([abs(lagrange_polynomial_0(y, n) - func(y)) for y in np.linspace(-1, 1, 1000)]))
        chebishev_approx.append(
            max([abs(lagrange_polynomial_1(y, n, -1, 1) - func(y)) for y in np.linspace(-1, 1, 1000)]))

    return (approx, chebishev_approx)


def configurate_graph(n):
    plt.subplot(1, 2, 1)
    x = np.arange(-5, 5.01, 0.001)
    plt.ylim([-0.05, 1])
    plt.xlim([-1.5, 1.5])
    plt.grid(True)
    plt.plot(x, abs(lagrange_polynomial_0(x, n) - func(x)), label=f"|P_{n}(x) - f(x)|")
    plt.plot(x, abs(lagrange_polynomial_1(x, n, -1, 1) - func(x)), color="red",
             label=f"|P_{n}(x) - f(x)| with Chebishev roots")
    plt.legend()
    plt.subplot(1, 2, 2)
    y = np.arange(2, 11, 1)
    plt.plot(y, count_approx()[0], label="Default")
    plt.plot(y, count_approx()[1], label="Chebishev")
    plt.legend()


for i in range(2, 11):
    configurate_graph(i)
    plt.show()

# configurate_graph(20)
# plt.show()
