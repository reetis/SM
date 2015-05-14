from math import sqrt

import numpy as np


def simpsons_method(function, int_begin: float, int_end: float, n: int) -> float:
    if n < 1:
        print("N turi būti ne mažesnis už 1")
        return None

    x = np.linspace(int_begin, int_end, n+1)

    result_sum = 0.0
    for i in range(1, n+1):
        result_sum += (function(x[i - 1]) + 4 * function((x[i - 1] + x[i]) / 2) + function(x[i])) * (x[i] - x[i - 1])

    return result_sum / 6


def gauss_quadrature_3(function, int_begin: float, int_end: float, n: int) -> float:
    if n < 1:
        print("N turi būti ne mažesnis už 1")
        return None

    x = np.linspace(int_begin, int_end, n+1)
    c1 = c3 = sqrt(0.6)
    c2 = 0

    result_sum = 0.0
    for i in range(1, n+1):
        beta = (x[i] - x[i - 1]) / 2
        alpha = (x[i] + x[i - 1]) / 2
        g = lambda s: function(beta * s + alpha)
        result_sum += beta * (5 * g(-c1) + 8 * g(c2) + 5 * g(c3)) / 9.

    return result_sum


def runge_error(sm: float, s2m: float, p: int) -> float:
    return abs(s2m - sm) / (2 ** p - 1)


def runge_kutta_midpoint(function, start: float, end: float, step: float, init_value: float) -> [(float, float)]:
    current_point = start
    result = [(current_point, init_value)]
    current_point += step
    while current_point < end+step/2:
        k1 = function(current_point, result[-1][1])
        k2 = function(current_point+step/2., result[-1][1] + step/2.*k1)
        result.append((current_point, result[-1][1]+step*k2))
        current_point += step
    return result
