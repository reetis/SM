import numpy as np

from uzd2.util import thomas_algorithm, convert_to_three_columns


ITER_LIMIT = 1000


def seidel_method(a, b, epsilon):
    error_calc = lambda x: max(abs(x))  #inf-norm
    first_req = check_diagonal_dominance(a) > 0
    second_req = check_symetry_and_positive_definite(a)
    if not (first_req or second_req):
        if not first_req:
            print("Matrica nėra su vyraujamąją įstrižaine")
        if not second_req:
            print("Matrica ne simetriška arba ne teigiamai apibrėžta")
        return None

    if second_req is 2:
        print("Paklaida skaičiuojama 1 normoje")
        error_calc = lambda x: np.sum(abs(x))
    else:
        print("Paklaida skaičiuojama inf normoje")

    x = np.zeros_like(b)

    print("Iteracijos:")
    for iter_count in range(ITER_LIMIT):
        new_x = np.zeros_like(x)
        for i in range(x.shape[0]):
            left = np.dot(a[i][:i], new_x[:i])
            right = np.dot(a[i][i + 1:], x[i + 1:])
            new_x[i] = (b[i] - (left + right)) / a[i][i]

        error = error_calc(new_x - x)
        x = new_x

        print("{}. {} -- Paklaida: {}".format(iter_count, x, error))

        if error < epsilon:
            return x

    print("Viršytas iteracijų limitas ({})".format(ITER_LIMIT))
    return x


def conjugate_gradient_method(a, f, epsilon):
    if not (check_symetry_and_positive_definite(a)):
        print("Matrica ne simetriška arba ne teigiamai apibrėžta")
        return None

    x = np.zeros_like(f)
    p = z = -f

    print("Iteracijos:")
    for iter_count in range(ITER_LIMIT):
        r = np.dot(a, p)
        alpha = np.dot(z, p) / np.dot(r, p)
        x = x - alpha * p
        new_z = z - alpha * r

        error = np.dot(new_z, new_z)
        print("{}. {} -- z = {} -- (z, z) = {}".format(iter_count, x, z, error))
        if error < epsilon ** 2:
            return x

        beta = error / np.dot(z, z)
        p = new_z + beta * p
        z = new_z

    print("Viršytas iteracijų limitas ({})".format(ITER_LIMIT))
    return x


def check_diagonal_dominance(matrix):
    abs_matrix = abs(matrix)
    diagonal = np.diagonal(abs_matrix)
    result = 0
    row_sums = np.sum(abs_matrix, axis=1) - diagonal
    col_sums = np.sum(abs_matrix, axis=0) - diagonal
    if np.all(diagonal > row_sums):
        result += 1         #Jei įstrižainė vyrauja eilutėse
    if np.all(diagonal > col_sums):
        result += 2         #Jei įstrižainė vyrauja stulpeliuose

    return result


def check_symetry_and_positive_definite(matrix):
    return np.all(matrix.T == matrix) and np.all(np.linalg.eigvals(matrix) > 0)


def inverse_iteration_method(a, lamb, epsilon):
    x = np.append(np.zeros(a.shape[0] - 1), [1])

    print("Iteracijos:")
    for iter_count in range(ITER_LIMIT):
        y = np.array(thomas_algorithm(convert_to_three_columns(a - np.identity(a.shape[0]) * lamb, x),
                                      check_matrix_compatibility=False))
        # y = seidel_method(a-np.identity(a.shape[0])*lamb, x, epsilon)
        # y = conjugate_gradient_method(a-np.identity(a.shape[0])*lamb, x, epsilon)
        new_x = y / np.linalg.norm(y)

        x_norm = np.linalg.norm(new_x - x)
        if x_norm + epsilon >= 2:
            new_x = -new_x
            x_norm = np.linalg.norm(new_x - x)

        new_lamb = np.dot(np.dot(a, new_x), new_x)

        print("{}. {} -- lambda = {} -- ||X_m+1 - X_m||= {}".format(iter_count, new_x, new_lamb, x_norm))
        if (x_norm <= epsilon) and (abs(new_lamb - lamb) <= epsilon):
            return new_lamb

        x = new_x
        lamb = new_lamb

    print("Viršytas iteracijų limitas ({})".format(ITER_LIMIT))
    return lamb
