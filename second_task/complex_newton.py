import numpy as np
import matplotlib.pyplot as plt


def example_2(z):
    return z ** 3 - 1


def example_2_df_dx(z):
    return 3 * z ** 2


def newtons_method(x_prev, func, diff_func, eps=1e-12):
    while True:
        x_new = x_prev - func(x_prev) / diff_func(x_prev)
        if abs(x_new - x_prev) < eps:
            return x_new
        x_prev = x_new


real = newtons_method(1000, example_2, example_2_df_dx)
cmp_1 = newtons_method(complex(0, 1000), example_2, example_2_df_dx)
cmp_2 = newtons_method(complex(0, -1000), example_2, example_2_df_dx)

size = 100
width, height = 800, 800
x_min, x_max = -size, size
y_min, y_max = -size, size

roots = [real, cmp_1, cmp_2]
print(roots)

x = np.linspace(x_min, x_max, width)
y = np.linspace(y_min, y_max, height)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y
colors = np.zeros((height, width, 3))

color = [(1, 1, 0), (0, 1, 1), (1, 0, 1)]


def closest_root_color(z):
    for i in range(len(roots)):
        if is_close(z, roots[i]):
            return color[i]
    return 1, 0, 0


def is_close(number_1, number_2, eps=1e-12):
    return np.abs(number_1 - number_2) < eps


for i in range(height):
    for j in range(width):
        z = Z[i, j]
        z = newtons_method(z, example_2, example_2_df_dx)
        colors[i, j] = closest_root_color(z)


def newtons_method_path(x_prev, func, diff_func, eps=1e-12):
    steps = []
    while True:
        steps.append(x_prev)
        x_new = x_prev - func(x_prev) / diff_func(x_prev)
        if abs(x_new - x_prev) < eps:
            steps.append(x_new)
            return steps
        x_prev = x_new


plt.imshow(colors, extent=(x_min, x_max, y_min, y_max))
plt.title('Newton method: z**3 - 1')


def add_paths(starts):
    for start in starts:
        steps = newtons_method_path(start, example_2, example_2_df_dx)
        print("root ", steps[-1])
        for i in steps:
            plt.scatter(i.real, i.imag)


s = [-75 + 0j, 0 + 75j, 46 - 68j]
add_paths(s)
plt.show()
