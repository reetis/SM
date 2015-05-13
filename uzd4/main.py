import matplotlib.pyplot as plt

from uzd4.util import *
from uzd4.config import *


function = lambda x: x*math.e**(2*x)
a = 0
b = 4

# ---------------------------------------------------------------------------------------------------------------------

N = init_N
results = [(N, simpsons_method(function, a, b, N), -1, -1)]
N *= 2
second_result = simpsons_method(function, a, b, N)
results.append((N, second_result, runge_error(results[-1][1], second_result, 4), -1))
N *= 2

while results[-1][2] > epsilon:
    result = simpsons_method(function, a, b, N)
    error = runge_error(results[-1][1], result, 4)
    results.append((N, result, error, results[-1][2] / error))
    N *= 2

print("{:-<80}".format(""))
print("{:-^80}".format(" Simpsono metodas "))
print("{:-<80}".format(""))

print("{:^9} | {:^19} | {:^19} | {:^19} |".format("N", "S_N", "Rungės paklaida", "Paklaidos pokytis"))
print("{:-<77}".format(""))
for result in results:
    print("{:>9d} | {:>19.12f} | {:>19.12f} | {:>19.12f} |".format(result[0], result[1], result[2], result[3]))

# ---------------------------------------------------------------------------------------------------------------------

N = init_N
results = [(N, gauss_quadrature_3(function, a, b, N), -1, -1)]
N *= 2
second_result = gauss_quadrature_3(function, a, b, N)
results.append((N, second_result, runge_error(results[-1][1], second_result, 4), -1))
N *= 2

while results[-1][2] > epsilon:
    result = gauss_quadrature_3(function, a, b, N)
    error = runge_error(results[-1][1], result, 4)
    results.append((N, result, error, results[-1][2] / error))
    N *= 2

print("{:-<80}".format(""))
print("{:-^80}".format(" Gauso kvadratūros metodas (3 eilės) "))
print("{:-<80}".format(""))

print("{:^9} | {:^19} | {:^19} | {:^19} |".format("N", "S_N", "Rungės paklaida", "Paklaidos pokytis"))
print("{:-<77}".format(""))
for result in results:
    print("{:>9d} | {:>19.12f} | {:>19.12f} | {:>19.12f} |".format(result[0], result[1], result[2], result[3]))

# ---------------------------------------------------------------------------------------------------------------------

function2 = lambda x, u: -u + math.sin(x)
h = 0.05*math.pi
u0 = 1
start = 0
end = math.pi

# h = float(input("Įveskite žingsnio dydį: "))
# u0 = float(input("Įveskite pradinę reikšmę: "))

result = runge_kutta_midpoint(function2, start, end, h, u0)
result2 = runge_kutta_midpoint(function2, start, end, h*2, u0)

x, y = zip(*result)
x2, y2 = zip(*result2)


plt.plot(x, y, 'b', x2, y2, 'r')
plt.legend(["h = {}".format(h), "h = {}".format(h*2)])
plt.xlabel("x")
plt.ylabel("u")


plt.show()
