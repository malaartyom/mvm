import numpy as np
import matplotlib.pyplot as plt


def display_7x7():
    C = np.matrix([[289, 2064, 336, 128, 80, 32, 16],
                   [1152, 30, 1312, 512, 288, 128, 32],
                   [-29, -2000, 756, 384, 1008, 224, 48],
                   [512, 128, 640, 0, 640, 512, 128],
                   [1053, 2256, -504, -384, -756, 800, 208],
                   [-287, -16, 1712, -128, 1968, -30, 2032],
                   [-2176, -287, -1565, -512, -541, -1152, -289]], dtype=int)

    L = np.matrix([[1, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 0],
                   [1, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0],
                   [0, 0, 1, 0, 1, 0, 0],
                   [1, 0, 0, 0, 0, 1, 0],
                   [0, 1, 1, 0, 1, 0, 1]], dtype=int)

    R = np.matrix([[1, 2048, 256, 128, 64, 32, 16],
                   [0, -2, 1024, 512, 256, 128, 32],
                   [0, 0, 4, 512, 1024, 256, 64],
                   [0, 0, 0, 0, 512, 512, 128],
                   [0, 0, 0, 0, -4, 1024, 256],
                   [0, 0, 0, 0, 0, 2, 2048],
                   [0, 0, 0, 0, 0, 0, -1]])
    print(np.linalg.inv(L) == L.transpose())
    print()
    F = np.linalg.inv(L).dot(R).dot(L)
    print(F)

def display_4x4():
    R_4 = np.matrix([[1, 2 ** 16, 256, 128],
                 [0, -2, 1024, 512],
                 [0, 0, 2, 2 ** 16],
                 [0, 0, 0, -1]])
    L_4 = np.matrix([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [1, 0, 1, 0],
                 [1, 1, 0, 1]], dtype=int)
    print(np.linalg.inv(L_4))
    print(L_4.transpose())

    C_4 = np.linalg.inv(L_4).dot(R_4).dot(L_4)
    eigvalues = np.linalg.eig(C_4)[0]
    print("Исходная матрица R со спtктром 1 -2 2 -1:")
    print(R_4)
    print()
    print("Матрица C = (L^-1)*R*L")
    print(C_4)
    print()
    print("Где L = ")
    print(L_4)
    print()
    print("Собственные числа матрицы С:", eigvalues)
    print(np.linalg.det(R_4))
    print(np.linalg.det(C_4))
    # plt.scatter([i.real for i in eigvalues], [i.imag for i in eigvalues])
    # plt.show()


    # print(np.linalg.eig(C)[0])

display_7x7()