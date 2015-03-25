import numpy
import matplotlib.pyplot as plt

from util import generate_cubic_splines


matrix = [
    [0,   1,    0,    0],
    [2,   10,   3,    60],
    [3,   8,    1,    192],
    [0,   1,    0,    0]
]

# print(thomas_algorithm(matrix))
splines = generate_cubic_splines([(0, 0), (1, 0.5), (2, 2), (3, 1.5)])

t1 = numpy.linspace(-1, 5, 500)
t2 = [splines(x) for x in t1]

plt.plot(t1, t2)
plt.scatter([0, 1, 2, 3], [0, 0.5, 2, 1.5])
plt.show()