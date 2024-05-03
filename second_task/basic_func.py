import math

epsilon = 10e-5


def example_1(x):
    return math.tan(x) - x


def example_1_df_dx(x):
    return 1 / (math.cos(x) ** 2) - 1


def example_1_fi(x, shift):
    if shift == 0:
        return math.atan(x) / 100
    return math.atan(x) + shift


def example_1_fi_v_2(x):
    return x - 0.001 * (math.tan(x) - x)


def dichotomy_method(f, lr):
    left, right = lr
    num_iters = 10000
    counter = 0
    if left > right:
        left, right = right, left
    for _ in range(num_iters):
        counter += 1
        mid = (left + right) / 2
        func_mid = f(mid)
        if abs(left - right) <= epsilon: return mid, counter
        if func_mid * f(left) > 0:
            left = mid
        else:
            right = mid
    return None, num_iters


def stop(x_prev, x_next):
    if abs(x_next - x_prev) < epsilon:
        return True
    return False


def simple_iterations(fi, x0, shift):
    x_prev = x0
    x_next = fi(x_prev, shift)
    counter = 0
    while not stop(x_prev, x_next):
        x_prev, x_next = x_next, fi(x_next, shift)
        counter += 1
    return x_next, counter


def simple_iterations_v_2(fi, x0):
    x_prev = x0
    x_next = fi(x_prev)
    counter = 0
    while not stop(x_prev, x_next):
        x_prev, x_next = x_next, fi(x_next)
        counter += 1
    return x_next, counter


def Newton_method(f, df_dx, xn):
    counter = 0
    while True:
        xn_1 = xn - f(xn) / df_dx(xn)
        if stop(xn, xn_1):
            return xn_1, counter
        xn = xn_1
        counter += 1


def k(f, x):
    return (x[-1] - x[-2]) / (f(x[-1]) - f(x[-2]))


def secant_method(f, xn):
    counter = 0
    shift = 0.00000001
    add = shift if xn > 0 else -shift
    x = [xn + add, xn]
    while True:
        xn_1 = xn - f(xn) * k(f, x)
        x.append(xn_1)
        if stop(xn, xn_1):
            return xn_1, counter
        xn = xn_1
        counter += 1


def inner_print(method: str, root: int, x: int, iterations: int) -> None:
    print(f'{method}: root {root}, x={x}, f(x)={example_1(x)}, num_iter={iterations}')


def close_root(f, root_range):
    result = []
    for i in root_range:
        result.append(get_root(f, i))
    return result


def get_root(f, root_num):
    shift = 0.1
    start = -math.pi / 2 + shift + math.pi * root_num
    end = math.pi / 2 - shift + math.pi * root_num
    while f(start) * f(end) > 0:
        start += shift
        end -= shift
    return start, end


def root_approximation(range_roots):
    initial_approximations = []
    for i in range_roots:
        sign = 1 if i >= 0 else -1
        approx = sign * ((math.pi / 2 - 0.1) + abs(i) * math.pi)
        initial_approximations.append(approx)
    return initial_approximations


# print("Enter roots range:")
# start = int(input("start: "))
# end = int(input("end: ")) + 1

# roots_num = range(start, end)

roots_num = range(-2, 3)  # Example

a = root_approximation(roots_num)

for root, i in enumerate(a):
    x, iterations = Newton_method(example_1, example_1_df_dx, i)
    inner_print("Newton method", roots_num[root], x, iterations)

print()
for root, i in enumerate(a):
    x, iterations = secant_method(example_1, i)
    inner_print("Secant method", roots_num[root], x, iterations)

print()
for root, i in enumerate(a):
    x, iterations = simple_iterations(example_1_fi, i, roots_num[root] * math.pi)
    inner_print("Simple iterations", roots_num[root], x, iterations)
print()

for root, i in enumerate(a):
    x, iterations = simple_iterations_v_2(example_1_fi_v_2, i)
    inner_print("Simple iterations v_2", roots_num[root], x, iterations)
print()

b = close_root(example_1, roots_num)
c = close_root_1(example_1, roots_num)
print(b)
print(c)

for root, i in enumerate(b):
    x, iterations = dichotomy_method(example_1, i)
    inner_print("Dichotomy_method ", roots_num[root], x, iterations)
