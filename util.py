import numpy

def simple_iter_method(function, starting_point, epsilon, max_derivative):
    iterations = []
    x = function(starting_point)
    old_x = starting_point
    accuracy = (1 - abs(max_derivative)) / abs(max_derivative) * epsilon
    iterations.append((old_x, x, abs(x - old_x)))
    print("{:<9d} | {:>15.12f} | {:>15.12f} | {:>15.12f} |".format(0, old_x, x, abs(x - old_x)))
    while abs(x - old_x) > accuracy:
        old_x = x
        x = function(x)
        iterations.append((old_x, x, abs(x - old_x)))
        print("{:<9d} | {:>15.12f} | {:>15.12f} | {:>15.12f} |".format(0, old_x, x, abs(x - old_x)))
    return x, iterations


def find_sol_interval(start, end, width, function1, function2):
    int_begin = start
    int_end = start + width
    intervals = []
    while int_end <= end:
        if (function1(int_begin) - function2(int_begin) > 0) != (function1(int_end) - function2(int_end) > 0):
            intervals.append( (int_begin, int_end) )

        int_begin = numpy.nextafter(int_end, int_end+1)
        int_end = int_end + width
    return intervals

def newton_method(function, function_derivative, starting_point, accuracy):
    iterations = []
    old_x = starting_point
    x = starting_point - function(starting_point)/function_derivative(starting_point)
    iterations.append((old_x, function(old_x), x, abs(x - old_x)))
    while abs(x - old_x) >= accuracy:
        old_x = x
        x = x - function(x)/function_derivative(x)
        iterations.append((old_x, function(old_x), x, abs(x - old_x)))
    return x, iterations