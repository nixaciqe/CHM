from math import *
print("Практическая работа 2")
def f(x):
    return (0.2 * x)**3 - cos(x)
a = 1.5
b = 1.6
eps = 0.001
while (b - a) / 2 > eps:
    c = (a + b) / 2
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
root = (a + b) / 2
print("Корень:", round(root, 6))
print()