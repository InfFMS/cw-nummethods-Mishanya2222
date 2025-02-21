from matplotlib import pyplot as plt
import numpy as np
import  math
lst_x = []
lst_y = []


R = 8.314
T = 273.15-130
a = 0.1382
b = 3.19*10**(-5)
P2 = 3664186.998
V = 10**(-5)

def eq(V):
    P = (R*T)/(V - b) - (a/(V**2)) - P2
    return P


# lst_x = np.arange(b + 10**(-5), 10**(-3))
# lst_y = eq(lst_x)

while V < 10**(-3):
    V = V + b
    if V == b:
        V = V + b
    lst_x.append(V)
    lst_y.append(eq(V))


def slove_equation(a2 ,b2,eps):
    while b2 - a2 >= 2*eps:
        c = (a2 + b2)/2
        if eq(a2)*eq(c) < 0:
            b2 = c
        else:
            a2 = c
    return c
# print(slove_equation(0.0000001, 0.001, 0.000001))
# XX= slove_equation(0.0000001, 0.001, 0.000001)
# plt.scatter(XX,eq(XX), color = "b")
plt.plot(lst_x, lst_y, 'r')
plt.grid()
plt.show()


print("First:",slove_equation(6*10**(-5),65*10**(-6),0.000001))
print("Second:",slove_equation(9*10**(-5),10**(-4),0.000001))
print("Third:",slove_equation(18*10**(-5),20*10**(-5),0.000001))
