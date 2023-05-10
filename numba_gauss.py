#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import array, concatenate
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box
import numpy as np

from numba import jit

@jit(nopython=True)
def gauss_elimination(A, B):
    n = A.shape[0]
    # Прямой ход метода Гаусса
    for pivot in range(n):
        for i in range(pivot + 1, n):
            factor = A[i, pivot] / A[pivot, pivot]
            for j in range(pivot + 1, n):
                A[i, j] -= factor * A[pivot, j]
            B[i] -= factor * B[pivot]
            A[i, pivot] = 0
    # Обратный ход метода Гаусса
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s += A[i, j] * x[j]
        x[i] = (B[i] - s) / A[i, i]
    return x


if __name__ == '__main__':
    np.random.seed(0)
    A = np.random.rand(1000, 1000)
    B = np.random.rand(1000)
    x = gauss_elimination(A, B)
    print(x)
# Очень быстрая обработка матрицы 1000х1000
