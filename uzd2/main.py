import numpy
import matplotlib.pyplot as plt
from scipy import interpolate

from uzd2.util import *
from uzd2.config import *


# print(thomas_algorithm(matrix))

print("---------------------------------------------------------------------------------------------------------------")
print(" Funkcijos ir splaino palyginimas")
print("---------------------------------------------------------------------------------------------------------------")
points = [(x, function(x)) for x in numpy.linspace(ival_a, ival_b, ival_points)]
print("Taškai: ", points)

print("----- Funkcijų generavimas")
splines = generate_cubic_splines(points)

print("----- Reikšmės tikrinimas taške")
print("x = %f" % checkpoint)
print("Originalus: y = %f" % function(checkpoint))
print("Splainas: y = %f" % splines(checkpoint))

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
print("x = %f" % bin_checkpoint)
print("Splainas: y = %f" % splines(bin_checkpoint))

t1 = numpy.linspace(0, 5, 500)
mine = [splines(x) for x in t1]

plt.subplot(212)
plt.plot(t1, mine, "b")
plt.title("Splainas iš tašku")
plt.scatter(x, y)
plt.show()