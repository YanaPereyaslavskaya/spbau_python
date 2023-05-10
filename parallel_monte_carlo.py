#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import partial
from multiprocessing import Pool, cpu_count
import random
import math

def count_points_in_circle(n):
    inside_circle = 0
    for i in range(n):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x * x + y * y <= 1:
            inside_circle += 1
    return inside_circle


def count_points_wrapper(args):
    return count_points_in_circle(args[0]),


def monte_carlo_pi_parallel(n):
    with Pool(cpu_count()) as p:
        results = p.map(count_points_wrapper, [(n // cpu_count(),) for _ in range(cpu_count())])
    return 4 * sum([r[0] for r in results]) / n


if __name__ == '__main__':
    a = monte_carlo_pi_parallel(100000)
    print(a, a - math.pi)
