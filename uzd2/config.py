matrix = [
    [0,   1,    0,    0],
    [2,   10,   3,    60],
    [3,   8,    1,    192],
    [0,   1,    0,    0]
]

function = lambda x: (2*x**2+6)/(x**2-2*x+5)
ival_a = -3
ival_b = 2
ival_points = 10
checkpoint = 1.5

# 50 = 0b110010
bin_points = [
    (0, 209),
    (1, 209),
    (2, 0),
    (3, 0),
    (4, 209),
    (5, 0)
]