from util import *
from config1 import *
import math, numpy
import matplotlib.pyplot as plt

if "period" not in locals():
    print("Nerastas nustatymas period")
    exit()
if "period_slices" not in locals():
    print("Nerastas nustatymas period_slices")
    exit()
if "epsilon" not in locals():
    print("Nerastas nustatymas epsilon")
    exit()

if type(period) is not int:
    print("Nustatymas period turi būti sveikas skaičius")
    exit()
if not(type(period_slices) is int or type(period_slices) is float):
    print("Nustatymas period_slices turi būti skaičius")
    exit()
if not(type(epsilon) is int or type(epsilon) is float):
    print("Nustatymas epsilon turi būti skaičius")
    exit()
if epsilon+1 == 1.0:
    print("Epsilon reikšmė per maža")
    exit()

interval_width = math.pi / period_slices
function = lambda x: math.tan(x)

print("{:-<80}".format(""))
print("{:-^80}".format(" Lygties x = tg(x) sprendinių paieška "))
print("{:-<80}".format(""))
print("Tikslumas:", epsilon)
print("Nagrinėjamas f-jos periodas:", period)
print("Ieškomo intervalo plotis:", interval_width)

print()
print("{:-<80}".format(""))
print("{:-^80}".format(" Intervalo su sprendiniu paieška "))
print("{:-<80}".format(""))

intervals = find_sol_interval(numpy.nextafter((period - 0.5) * math.pi, (period - 0.5) * math.pi + 1).item(),
                              numpy.nextafter((period + 0.5) * math.pi, (period - 0.5) * math.pi - 1).item(),
                              interval_width, function, lambda x: x)

if len(intervals) != 1:
    print("Netinkamas rastų intervalų kiekis:", len(intervals))
    print("Intervalai:", intervals)
else:
    print("Sprendinys turėtų būti intervale [{};{}]".format(intervals[0][0], intervals[0][1]))

print()
print("{:-<80}".format(""))
print("{:-^80}".format(" Paprastųjų iteracijų metodas "))
print("{:-<80}".format(""))
function = lambda x: math.atan(x) + period * math.pi
function_derivative = lambda x: 1 / (x ** 2 + 1)

if period != 0:
    if period == 0:
        print("Pertvarkyta lygtis: x=arctg(x)")
    else:
        print("Pertvarkyta lygtis: x=arctg(x){:+d}*pi".format(period))
    print("Išvestinė: 1/(x^2+1)")

    max_derivative = None
    if intervals[0][0] > 0:
        max_derivative = function_derivative(intervals[0][0])
    else:
        max_derivative = function_derivative(intervals[0][1])

    print("q =", abs(max_derivative))

    rez = simple_iter_method(function, intervals[0][0], epsilon, max_derivative)
    print()
    print("{:^9} | {:^19} | {:^19} | {:^19} |".format("Iteracija", "x", "g(x)", "Paklaida"))
    print("{:-<77}".format(""))
    for index, iteration in enumerate(rez[1]):
        print("{:<9d} | {:>19.12f} | {:>19.12f} | {:>19.12f} |".format(index + 1, iteration[0], iteration[1], iteration[2]))
    print("Lygties sprendinys:", rez[0])
else:
    print("Šiame intervale paprastųjų iteracijų metodas neveikia (išvestinė, kai x=0, yra 0)")

print()
print("{:-<80}".format(""))
print("{:-^80}".format(" Niutono metodas "))
print("{:-<80}".format(""))
function = lambda x: math.tan(x)-x
function_derivative = lambda x: math.tan(x)**2
try:
    rez = newton_method(function, function_derivative, intervals[0][0], epsilon)
    print("Pertvarkyta lygtis: tg(x)-x=0")
    print("Išvestinė: tg(x)^2")
    print()
    print("{:^9} | {:^19} | {:^19} | {:^19} | {:^19} |".format("Iteracija", "x_i", "f(x)", "x_i+1", "Paklaida"))
    print("{:-<99}".format(""))
    for index, iteration in enumerate(rez[1]):
        print("{:<9d} | {:>19.12f} | {:>19.12f} | {:>19.12f} | {:>19.12f} |".format(index + 1, iteration[0], iteration[1],
                                                                                    iteration[2], iteration[3]))
    print("Lygties sprendinys:", rez[0])
except ValueError:
    print("Šis metodas nerado tinkamos reikšmės")

def f(t):
    return numpy.exp(-t) * numpy.cos(2*numpy.pi*t)

t1 = numpy.linspace(-15, 15, 500)

plt.figure(1)
plt.subplot(321)
plt.title("x = tg(x)")
plt.plot(t1, numpy.tan(t1), 'b', t1, t1, 'r', t1, t1-t1, 'k', t1-t1, t1, 'k')
plt.ylim(-15, 15)
plt.xticks(numpy.arange(-15, 15, 1.5))
plt.yticks(numpy.arange(-15, 15, 4))

plt.subplot(322)
plt.title("(tg(x))'")
plt.plot(t1, 1/numpy.cos(t1)**2, 'b', t1, t1-t1, 'k', t1-t1, t1, 'k')
plt.ylim(-15, 15)
plt.xticks(numpy.arange(-15, 15, 1.5))
plt.yticks(numpy.arange(-15, 15, 4))

plt.subplot(323)
plt.title("x = arctg(x)")
plt.plot(t1, numpy.arctan(t1), 'b', t1, t1, 'r', t1, t1-t1, 'k', t1-t1, t1, 'k')
plt.ylim(-1.5, 1.5)
plt.xticks(numpy.arange(-15, 15, 1.5))
plt.yticks(numpy.arange(-1.5, 1.5, 0.3))

plt.subplot(324)
plt.title("(arctg(x))'")
plt.plot(t1, 1/(1+t1**2), 'b', t1, t1-t1+1, 'r', t1, t1-t1, 'k', t1-t1, t1, 'k')
plt.ylim(-1.5, 1.5)
plt.xticks(numpy.arange(-15, 15, 1.5))
plt.yticks(numpy.arange(-1.5, 1.5, 0.2))

plt.subplot(325)
plt.title("tg(x) - x = 0")
plt.plot(t1, numpy.tan(t1) - t1, 'b', t1, t1-t1, 'k', t1-t1, t1, 'k')
plt.ylim(-15, 15)
plt.xticks(numpy.arange(-15, 15, 1.5))
plt.yticks(numpy.arange(-15, 15, 4))
plt.show()