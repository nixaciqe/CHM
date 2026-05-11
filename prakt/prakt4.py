from math import *
print("практическая работа 4")
def f(x):
    return (0.2 * x)**3 - cos(x)
def f_prime(x):
    return 0.024 * x**2 + sin(x)
x0 = 1.6
while True:
    x1 = x0 - f(x0) / f_prime(x0)
    if abs(x1 - x0) < 0.001:
        break
    x0 = x1
print("Корень (касательных):", round(x1, 6))
print()
print("Метод хорд")
a = 1.5
b = 1.6
while True:
    c = a - f(a) * (b - a) / (f(b) - f(a))
    if abs(c - a) < 0.001:
        break
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
print("Корень (хорд):", round(c, 6))