import sys
from util import *
import math, numpy

period = 3
interval_width = math.pi / 18
epsilon = 0.0000001
function = lambda x: math.atan(x) + period * math.pi
function_derivative = lambda x: 1 / (x ** 2 + 1)

print("{:-<80}".format(""))
print("{:-^80}".format(" Lygties x = tg(x) sprendinių paieška "))
print("{:-<80}".format(""))
print("Tikslumas:", epsilon)
print("Nagrinėjamas f-jos periodas:", period)
print("Ieškomo intervalo plotis:", interval_width)
if period == 0:
    print("Pertvarkyta f-ja: x=arctg(x)")
else:
    print("Pertvarkyta f-ja: x=arctg(x){:+d}*pi".format(period))
print("Pertvarkytos f-jos išvestinė: 1/(x^2+1)")

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
    print("Sprendinys turėtų būti intervale", intervals[0])

print()
print("{:-<80}".format(""))
print("{:-^80}".format(" Paprastųjų iteracijų metodas "))
print("{:-<80}".format(""))

if period != 0:
    max_derivative = None
    if intervals[0][0] > 0:
        max_derivative = function_derivative(intervals[0][0])
    else:
        max_derivative = function_derivative(intervals[0][1])

    rez = simple_iter_method(function, intervals[0][0], epsilon, max_derivative)

    print("{:^9} | {:^15} | {:^15} | {:^15} |".format("Iteracija", "x", "g(x)", "Paklaida"))
    print("{:-<65}".format(""))
    for index, iteration in enumerate(rez[1]):
        print("{:<9d} | {:>15.12f} | {:>15.12f} | {:>15.12f} |".format(index + 1, iteration[0], iteration[1], iteration[2]))
    print("Lygties sprendinys:", rez[0])
else:
    print("Šiame intervale paprastųjų iteracijų metodas neveikia (išvestinė, kai x=0, yra 0)")

print()
print("{:-<80}".format(""))
print("{:-^80}".format(" Niutono metodas "))
print("{:-<80}".format(""))

rez = newton_method(lambda x: math.tan(x)-x, lambda x: math.tan(x)**2, intervals[0][0], epsilon)

print("{:^9} | {:^15} | {:^15} | {:^15} | {:^15} |".format("Iteracija", "x_i", "f(x)", "x_i+1", "Paklaida"))
print("{:-<83}".format(""))
for index, iteration in enumerate(rez[1]):
    print("{:<9d} | {:>15.12f} | {:>15.12f} | {:>15.12f} | {:>15.12f} |".format(index + 1, iteration[0], iteration[1],
                                                                                iteration[2], iteration[3]))
print("Lygties sprendinys:", rez[0])
