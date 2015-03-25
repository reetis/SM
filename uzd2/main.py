import numpy
import matplotlib.pyplot as plt
from scipy import interpolate

from uzd2.util import *
from uzd2.config import *


# print(thomas_algorithm(matrix))

# ----------------------------------------------------------------------------------------------------------------------
# Funkcijos ir splaino palyginimas
# ----------------------------------------------------------------------------------------------------------------------
points = [(x, function(x)) for x in numpy.linspace(ival_a, ival_b, ival_points)]
splines = generate_cubic_splines(points)

print("x = %f" % checkpoint)
print("Originalus: y = %f" % function(checkpoint))
print("Interpoliuotas: y = %f" % splines(checkpoint))

t1 = numpy.linspace(ival_a - 1, ival_b + 1, 500)
interpolated = [splines(x) for x in t1]
original = [function(x) for x in t1]

x, y = zip(*points)

plt.subplot(211)
plt.plot(t1, original, "b", t1, interpolated, "r")
plt.legend(["Tikroji f-ja", "Kubinis splainas"])
plt.title("Funkcijos ir splaino palyginimas")
plt.scatter(x, y)

# ----------------------------------------------------------------------------------------------------------------------
# Splainas iš duotų taškų
# ----------------------------------------------------------------------------------------------------------------------
x, y = zip(*bin_points)

splines = generate_cubic_splines(bin_points)
spline_ref = interpolate.interp1d(x, y, kind="cubic")

print("x = %f" % checkpoint)
print("Mano splainas: y = %f" % splines(checkpoint))
print("Scipy splainas: y = %f" % spline_ref(checkpoint))

t1 = numpy.linspace(0, 5, 500)
mine = [splines(x) for x in t1]

plt.subplot(212)
plt.plot(t1, mine, "b", t1, spline_ref(t1), "r")
plt.legend(["Mano Splainas", "Scipy splainas"])
plt.title("Splainas iš tašku")
plt.scatter(x, y)
plt.show()