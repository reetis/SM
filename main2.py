from util2 import thomas_algorithm, generate_cubic_splines

matrix = [
    [0,   1,    0,    0],
    [2,   10,   3,    60],
    [3,   8,    1,    192],
    [0,   1,    0,    0]
]

# print(thomas_algorithm(matrix))
generate_cubic_splines([(0, 0), (1, 0.5), (2, 2), (3, 1.5)])