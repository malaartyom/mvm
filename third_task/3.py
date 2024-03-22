import numpy as np
import time
import matplotlib.pyplot as plt

def func(x):
    return 1 / (1 + 25 * x ** 2)

def get_roots(n):
    answ = []
    for i in range(n + 1):
        answ.append(((2 * i) / n) - 1) 
    return answ

def get_chebishev_roots(n, a, b):
    answ = []
    for i in range(n + 1):
        answ.append(0.5 * (b + a) + 0.5 * (b - a) * np.cos(((2 * i  + 1) * np.pi) / (2 * (n + 1))))
    return answ


def lagrange_polynomial_0(x, n):
    roots = get_roots(n)
    answ = 0
    for i, root in enumerate(roots):
        answ += (func(root) * w(x, roots)) / ((x - root) * dw(root, i, roots))
    return answ


def lagrange_polynomial_1(x, n, a, b):
    roots = get_chebishev_roots(n, a, b)
    answ = 0
    for i, root in enumerate(roots):
        answ += (func(root) * w(x, roots)) / ((x - root) * dw(root, i, roots))
    return answ

def w(x, roots):
    answ = 1
    for root in roots:
        answ *= (x - root)
    return answ

def dw(x_i, i, roots):
    answ = 1
    for j, root in enumerate(roots):
        if j != i:
            answ *= (x_i - root)
    return answ

# x = np.arange(-5, 5.01, 0.01)
# plt.ylim([-0.05, 0.5])  
# plt.xlim([-1.5, 1.5]) 
# plt.grid(True)
for n in range(3, 11):
    fig, ax = plt.subplots()
    fig.set_size_inches(10,8)
    x = np.arange(-5, 5.01, 0.01)
    plt.ylim([-0.05, 1])  
    plt.xlim([-1.5, 1.5]) 
    plt.grid(True)
    plt.plot(x, abs(lagrange_polynomial_0(x, n) - func(x)), label=f"|P_{n}(x) - f(x)|")
    plt.plot(x, abs(lagrange_polynomial_1(x, n, 1.5, -1.5) - func(x)), color="red", label=f"|P_{n}(x) - f(x)| with Chebishev roots")
    plt.legend()
    plt.show()

# plt.plot(x, abs(lagrange_polynomial_0(x, 5) - func(x)))
# plt.plot(x, abs(lagrange_polynomial_0(x, 10) - func(x)), '--g')
# plt.plot(x, abs(lagrange_polynomial_1(x, 10, 1.5, -1.5) - func(x)), color="red")
# plt.legend(("|P_4(x) - f(x)|", "|P10(x) - f(x)|", "|P10(x) - f(x)| with Chebishev roots"))
# plt.grid(True)