#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
import math


def monte_carlo_pi(n):  # считаем число π с помощью метода Монте-Карло
    k = 0
    for i in range(n):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x * x + y * y <= 1:
            k += 1
    return 4 * k / n


if __name__ == '__main__':
    a = monte_carlo_pi(10000)
    print(a, a - math.pi)
