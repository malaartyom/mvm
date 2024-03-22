from typing import Tuple
def get_roots(a: float, N: float, h: float):
    roots = []
    for i in range(N + 1):
        roots.append(a + i * h)

    return roots


def integrate_Simpson(func, a, b, N: int):
    h = (b - a) / N
    roots = get_roots(a, N, h)

    answer = 0
    for i in range(1, N, 2):
        answer += func(roots[i - 1]) + 4 * func(roots[i]) + func(roots[i + 1])

    return (h * answer) / 3


def func(x): 
    return x ** 4
if __name__ == "__main__":
    print(integrate_Simpson(func, 0, 2, 10))
    


