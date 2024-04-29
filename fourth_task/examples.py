from simpson_integrate import integrate_simpson
from math import sin, pi, e, sqrt, inf
from scipy import integrate


def count_approximation(func, order: int, amount_of_steps: int, r):
    F = integrate_simpson
    return abs((F(func, 0, 1, amount_of_steps) - F(func, 0, 1, amount_of_steps // r)) / ((r ** order) - 1))


def func1(x):
    if x == 0:
        return pi
    elif x == 1:
        return 5 * pi
    return (sin(pi * x ** 5)) / ((x ** 5) * (1 - x))


def func2(x):
    return e ** (-sqrt(x) + sin(x / 10))


def test_first():
    print()
    # for n in range(1, 17):
    #     print(f"n = {n} -----------------------------")
    #     actual = integrate_simpson(func1, 0, 1, 1000)
    #     expected = integrate.quad(func1, 0, 1)[0]
    #     print(f"actual = {actual}, expected = {expected}")
    #     print("delta =", abs(actual - expected))
    #     print("-----------------------------------")

    actual = integrate_simpson(func1, 0, 1, 1000)
    expected = integrate.quad(func1, 0, 1)[0]
    print(f"actual = {actual}, expected = {expected}")
    approximation = count_approximation(func1, 4, 10 ** 5, 10)
    approximation1 = count_approximation(func1, 4, 10 ** 5, 20)
    print(approximation / approximation1)
    print("approximation= ", approximation)
    assert (approximation < 10 ** -8)


def test_second():
    actual = integrate_simpson(func2, 0, inf, 10 ** 5)
    expected = integrate.quad(func2, 0, inf)[0]
    print()
    print(f"actual = {actual}, expected = {expected}")
    print("delta =", abs(actual - expected))
    approximation = count_approximation(func2, 5, 1000, 10)
    print("approximation= ", approximation)
    assert (approximation < 10 ** -8)


if __name__ == "__main__":
    test_first()
    test_second()
