import numpy
import matplotlib.pyplot as plt

from uzd2.util import *
from uzd2.config import *

print("---------------------------------------------------------------------------------------------------------------")
print(" Triistrižainių matricų sprendimas")
print("---------------------------------------------------------------------------------------------------------------")

def print_matrix_result(matrix):
    try:
        result = thomas_algorithm(matrix)
        print("Rezultatas:", result)
    except ValueError as e:
        print("Šitos matricos negalima išspręsti:", e)

print("Pirmos matricos rezultatas:")
print_matrix_result(matrix1)
print("Pirmos a matricos rezultatas:")
print_matrix_result(matrix1a)
print("Antros matricos rezultatas:")
print_matrix_result(matrix2)
print("Trečios matricos rezultatas:")
print_matrix_result(matrix3)

print("---------------------------------------------------------------------------------------------------------------")
print(" Funkcijos ir splaino palyginimas")
print("---------------------------------------------------------------------------------------------------------------")
points = [(x, function(x)) for x in numpy.linspace(ival_a, ival_b, ival_points)]
print("Taškai: ", points)

print("----- Funkcijų generavimas")
splines = generate_cubic_splines(points)

print("----- Reikšmės tikrinimas taške")
try:
    point = float(input("Įveskite tašką:"))

    print("x =", point)
    print("Originalus: y =", function(point))
    print("Splainas: y =", splines(point))
    if point < ival_a or point > ival_b:
        print("Taškas neįeina į intervalą [{};{}]".format(ival_a, ival_b))
except ValueError:
    print("Įvestis ne skaičius")

t1 = numpy.linspace(ival_a - 1, ival_b + 1, 500)
interpolated = [splines(x) for x in t1]
original = [function(x) for x in t1]

x, y = zip(*points)

plt.subplot(211)
plt.plot(t1, original, "b", t1, interpolated, "r")
plt.legend(["Tikroji f-ja", "Kubinis splainas"])
plt.title("Funkcijos ir splaino palyginimas")
plt.scatter(x, y)

print("---------------------------------------------------------------------------------------------------------------")
print(" Splainas iš duotų taškų")
print("---------------------------------------------------------------------------------------------------------------")

x, y = zip(*bin_points)
print("Taškai: ", bin_points)

print("----- Funkcijų generavimas")
splines = generate_cubic_splines(bin_points)

print("----- Reikšmės tikrinimas taške")
try:
    point = float(input("Įveskite tašką:"))

    print("x =", point)
    print("Splainas: y =", splines(point))
    if point < 0 or point > 5:
        print("Taškas neįeina į intervalą [0;5]")
except ValueError:
    print("Įvestis ne skaičius")

t1 = numpy.linspace(0, 5, 500)
mine = [splines(x) for x in t1]

plt.subplot(212)
plt.plot(t1, mine, "b")
plt.title("Splainas iš tašku")
plt.scatter(x, y)
plt.show()