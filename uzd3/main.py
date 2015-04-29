from uzd3.config import *
from uzd3.util import *

B = np.array(B)
C = np.array(C)
D = np.array(D)

A = D + C * id_number

test_A1 = np.array([
    [4., -1., -1.],
    [6., 8., 0.],
    [-5., 0., 12.]
])
test_B1 = np.array([-2., 45., 80.])

test_A2 = np.array([
    [2, 1, 0.95],
    [1, 2, 1],
    [0.95, 1, 2]
])
test_B2 = np.array([3.95, 4, 3.95])

check_diagonal_dominance(np.array([[7, -1, 1, -3], [1, -10, -6, 2], [-2, 2, 12, 3], [-3, 5, -3, 9]]))

print("----------- Gauso-Zeidelio metodas ----------------------------------------------------------------------------")
result = seidel_method(A, B, epsilon)
print("Rezultatas: {}\n".format(result))

print("----------- Jungtinių gradientų metodas -----------------------------------------------------------------------")
result = conjugate_gradient_method(A, B, epsilon)
print("Rezultatas: {}\n".format(result))


print("----------- Jungtinių gradientų metodas -----------------------------------------------------------------------")
T = np.array(T)
C2 = np.array(C2)

A2 = T + C2 * id_number
print("Matrica A:\n{}".format(A2))

lamb = float(input("Įveskite pradinę lambdą reikšmę: "))
result = inverse_iteration_method(A2, lamb, epsilon)
print("Rezultatas: lambda = {}".format(result))