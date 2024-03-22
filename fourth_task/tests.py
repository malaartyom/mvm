from scipy import integrate
from simpson_integrate import integrate_simpson
import math
from colorama import Fore

funcs = [(math.sin, 0, math.pi / 4)]


def run_test(i, N):
    func, a, b = funcs[i]
    expected = integrate.quad(func, a, b)[0]
    actual = integrate_simpson(func, a, b, N)
    h = (b - a) / N
    assert (abs(expected - actual) < h ** 4)
    print(Fore.GREEN + f"TEST {i} with N = {N} HAVE PASSED", )


def test_0():
    run_test(0, 10)


def test_1():
    run_test(0, 1000)


if __name__ == "__main__":
    test_0()
    test_1()
