#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import array, concatenate
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box


def gauss_elimination(A, B):
    n = len(A)
    # Прямой ход метода Гаусса
    for pivot in range(n):
        for i in range(pivot + 1, n):
            factor = A[i][pivot] / A[pivot][pivot]
            for j in range(pivot + 1, n):
                A[i][j] -= factor * A[pivot][j]
            B[i] -= factor * B[pivot]
            A[i][pivot] = 0
    # Обратный ход метода Гаусса
    x = [0] * n
    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s += A[i][j] * x[j]
        x[i] = (B[i] - s) / A[i][i]
    return x


#  print(multiply(array([[1, 2], [3, 4]]), array([2])))
if __name__ == '__main__':
    a = array([
        [1.5, 2.0, 1.5, 2.0],
        [3.0, 2.0, 4.0, 1.0],
        [1.0, 6.0, 0.0, 4],
        [2.0, 1.0, 4.0, 3]
    ], dtype=float)

    b = array([5, 6, 7, 8], dtype=float)

    solution = gauss_elimination(a, b)
    oob_solution = solve_out_of_the_box(a, b)

    print(solution)
    print("Макс отклонение компоненты решения:", norm(solution - oob_solution, ord=1))
