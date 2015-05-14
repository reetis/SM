import math

init_N = 1
end_N = 256
function = lambda x: (math.e ** x - 1) / (math.e ** x + 1)
a = 1
b = 2

function2 = lambda x, u: math.cos(x+u) + 1.5*(x-u)
max_h = 1
min_h = 0.0001
u0 = 1
start = 0
end = 1