from fractions import Fraction
from functools import partial

import numpy as np


def thomas_algorithm(matrix, check_matrix_compatibility=True):
    # Check if applicable
    if check_matrix_compatibility:
        has_strict = False
        for a, b, c, d in matrix:
            if abs(b) < abs(a) + abs(c):
                raise ValueError("Turi būti netenkinama šita nelygybė |b_i| < |a_i| + |c_i|")
            elif abs(b) > abs(a) + abs(c):
                has_strict = True

        if not has_strict:
            raise ValueError("Su bent vienu i turi būti tenkinama šita sąlyga |b_i| > |a_i| + |c_i|")

    matrix = map(partial(map, lambda x: Fraction(x).limit_denominator()), matrix)

    # Forward propagation
    C = []
    D = []
    for a, b, c, d in matrix:
        if len(C) is 0:
            C.append(Fraction(-c, b))
            D.append(Fraction(d, b))
        else:
            denominator = a * C[-1] + b
            D.append(Fraction(d - a * D[-1], denominator))
            C.append(Fraction(-c, denominator))

    # Backward propagation
    x = []
    for Ci, Di in zip(reversed(C), reversed(D)):
        if len(x) is 0:
            x.append(Di)
        else:
            x.append(Ci * x[-1] + Di)

    return list(reversed([float(nr) for nr in x]))


def generate_cubic_splines(values):
    def get_spline(e, G, H, xi, yi):
        return lambda x: yi + e * (x - xi) + G * (x - xi) ** 2 + H * (x - xi) ** 3

    xs, ys = zip(*values)

    h = []
    for index in range(len(values) - 1):
        h.append(xs[index + 1] - xs[index])

    f = []
    for index in range(len(h)):
        f.append((ys[index + 1] - ys[index]) / h[index])

    matrix = []
    for index in range(len(values)):
        if index is 0 or index is len(values) - 1:
            matrix.append([0, 1, 0, 0])
        else:
            matrix.append([h[index - 1], 2 * (h[index] + h[index - 1]), h[index], 6 * (f[index] - f[index - 1])])

    g = thomas_algorithm(matrix)
    print("g reikšmės: ", g)

    functions = []
    for index in range(len(h)):
        e = f[index] - g[index + 1] * h[index] / 6 - g[index] * h[index] / 3
        G = g[index] / 2
        H = (g[index + 1] - g[index]) / (6 * h[index])
        print(
            "S{0}(x) = {1} + {3}*(x-{2}) + {4}*(x-{2})^2 + {5}*(x-{2})^3".format(index, ys[index], xs[index], e, G, H))
        functions.append(get_spline(e, G, H, xs[index], ys[index]))

    return partial(composite_function, values, functions)


def composite_function(values, functions, x):
    dict_values = dict(values)
    if x in dict_values:
        return dict_values[x]

    for index, val in enumerate(values):
        if index is 0 and x < val[0]:
            # raise ValueError("Funkcija su %.f neapibrėžta" % x)
            return None
        elif x < val[0]:
            return functions[index - 1](x)

    # raise ValueError("Funkcija su %.f neapibrėžta" % x)
    return None


def convert_to_three_columns(coff_matrix, right_side):
    first_diag = np.append([0], np.diagonal(coff_matrix, offset=-1))
    second_diag = np.diagonal(coff_matrix)
    third_diag = np.append(np.diagonal(coff_matrix, offset=1), [0])

    result = np.append(np.array([first_diag]).T, np.array([second_diag]).T, axis=1)
    result = np.append(result, np.array([third_diag]).T, axis=1)
    result = np.append(result, np.array([right_side]).T, axis=1)

    return result