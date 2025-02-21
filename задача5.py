
from matplotlib import pyplot as plt
import math

num = int(input('введите какая функция'))
R = 8.314
T = 273.15-130
a = 0.1382
b = 3.19*10**(-5)
P2 = 3664186.998
V = 10**(-5)

def eq(V):
    if num == 1:
        P = (R * T) / (V - b) - (a / (V ** 2))
    if num == 2:
        P = 3664186.998
    return P

integ = 0
while V < 10**(-3):
    V = V + b
    integ = integ + (((eq(V) + eq(V+b))/2)*b)

print(integ)
