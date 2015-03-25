from fractions import Fraction
from functools import partial


def thomas_algorithm(matrix):
    # Check if applicable
    has_strict = False
    for a, b, c, d in matrix:
        if abs(b) < abs(a) + abs(c):
            raise ValueError("|b_i| < |a_i| + |c_i| has occurred")
        elif abs(b) > abs(a) + abs(c):
            has_strict = True

    if not has_strict:
        raise ValueError("|b_i| > |a_i| + |c_i| has not occurred")

    matrix = map(partial(map, lambda x: Fraction(x).limit_denominator()), matrix)

    # Forward propagation
    C = []
    D = []
    for a, b, c, d in matrix:
        if len(C) is 0:
            C.append(Fraction(-c, b))
            D.append(Fraction(d, b))
        else:
            D.append(Fraction(d-a*D[-1], a*C[-1]+b))
            C.append(Fraction(-c, a*C[-1]+b))

    # Backward propagation
    x = []
    for Ci, Di in zip(reversed(C), reversed(D)):
        if len(x) is 0:
            x.append(Di)
        else:
            x.append(Ci*x[-1]+Di)

    return list(reversed([float(nr) for nr in x]))


def generate_cubic_splines(values):
    xs, ys = zip(*values)

    h = []
    for index in range(len(values)-1):
        h.append(xs[index+1] - xs[index])

    f = []
    for index in range(len(h)):
        f.append((ys[index+1] - ys[index])/h[index])

    g = [0, 2.4, -3.6, 0]

    functions = []
    for index in range(len(h)):
        e = f[index] - g[index+1]*h[index]/6 - g[index]*h[index]/3
        G = g[index]/2
        H = (g[index+1] - g[index]) / (6*h[index])
        functions.append(get_spline(e, G, H, xs[index], ys[index]))

    return partial(composite_function, values, functions)

def get_spline(e, G, H, xi, yi):
    return lambda x: yi + e*(x-xi) + G*(x-xi)**2 + H*(x-xi)**3



def composite_function(values, functions, x):
    dict_values = dict(values)
    if x in dict_values:
        return dict_values[x]

    for index, val in enumerate(values):
        if index is 0 and x < val[0]:
            # raise ValueError("Funkcija su %.f neapibrėžta" % x)
            return None
        elif x < val[0]:
            return functions[index-1](x)

    # raise ValueError("Funkcija su %.f neapibrėžta" % x)
    return None