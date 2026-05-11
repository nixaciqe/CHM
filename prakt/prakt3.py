from math import *

print("Практическая работа 3")

def phi(x):
    return acos((0.2 * x)**3)

x0 = 1.5

for i in range(100):
    x1 = phi(x0)
    if abs(x1 - x0) < 0.001:
        break
    x0 = x1

print("Корень:", round(x1, 6))