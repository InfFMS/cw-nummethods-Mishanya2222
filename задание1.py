# Построить графики уравнения Ван-дер-Ваальса при температурах -140, -130, -120, -110, -100
# градусов Цельсия. Выделить красным цветом кривую, начиная с которой начинаются
# изменения в поведении функции (см. пояснение).
import numpy
from matplotlib import pyplot as plt
import  math
lst_x = []

lst_y = []
R = 8.31
#[P + a (n2/V2)] (V - nb) = nRT
a = 0.1382
b = 3.19*10**(-5)
t = int(input())


def eq(V,T):
    P = -(R*T)/(V - b) - (a/(V**2))
    return P



if t ==1:
    T = -133
elif t == 2:
    T = -143
elif t == 3:
    T = -153
elif t == 4:
    T = -163
elif t == 5:
    T = -173

V = 10**(-5)
while V < 10**(-3):
    V = V + b
    lst_x.append(V)
    lst_y.append(eq(V, T))



plt.plot(lst_x, lst_y, 'r')
plt.grid()
plt.show()




