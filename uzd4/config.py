import math

init_N = 2
function = lambda x: (math.e ** x - 1) / (math.e ** x + 1)
a = 1
b = 2

epsilon = 0.000001

function2 = lambda x, u: math.cos(x+u) + 1.5*(x-u)