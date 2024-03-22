from simpson_integrate import integrate_simpson
from math import sin, pi, e, sqrt, inf
from scipy import integrate


def func1(x):
    return (sin(pi * x ** 5)) / ((x ** 5) * (1 - x))


def func2(x):
    return e ** (-sqrt(x) + sin(x / 10))


def test_first():
    print()
    for n in range(1, 17):
        print(f"n = {n} -----------------------------")
        actual = integrate_simpson(func1, 10 ** -n, 1 - 10 ** -n, 1000)
        expected = integrate.quad(func1, 0, 1)[0]
        print(f"actual = {actual}, expected = {expected}")
        print("delta =", abs(actual - expected))
        print("-----------------------------------")

    actual = integrate_simpson(func1, 10 ** -10, 1 - 10 ** -10, 1000)
    expected = integrate.quad(func1, 0, 1)[0]
    assert (abs(actual - expected) < 10 ** -8)


def test_second():
    actual = integrate_simpson(func2, 0, inf, 100000)
    expected = integrate.quad(func2, 0, inf)[0]
    print()
    print(f"actual = {actual}, expected = {expected}")
    print("delta =", abs(actual - expected))
    assert (abs(actual - expected) < 10 ** -8)


if __name__ == "__main__":
    test_first()
    test_second()
