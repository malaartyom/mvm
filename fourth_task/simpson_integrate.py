import math


def get_roots(a: float, N: int, h: float):
    roots = []
    for i in range(N + 1):
        roots.append(a + i * h)

    return roots


def integrate_simpson(function, a, b, N: int):
    func1 = function
    if b == math.inf:
        def f(t):
            return function(t / (1 - t)) / ((1 - t) ** 2)

        func1 = f
        b = 1 - 10 ** -10
        a = a / (a - 1)

    h = (b - a) / N
    roots = get_roots(a, N, h)

    answer = 0
    for i in range(1, N, 2):
        answer += func1(roots[i - 1]) + 4 * func1(roots[i]) + func1(roots[i + 1])

    return (h * answer) / 3


def func(x):
    return x ** 4


if __name__ == "__main__":
    print(integrate_simpson(func, 0, 2, 10))
