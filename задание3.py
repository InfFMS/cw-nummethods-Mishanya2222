import numpy
from matplotlib import pyplot as plt
import  math
lst_x = []

lst_y = []
R = 8.31
#[P + a (n2/V2)] (V - nb) = nRT
a = 0.1382
b = 3.19*10**(-5)
T = 143.15





def eq(V):
    P = (R*T)/(V - b) - (a/(V**2))
    return P





V = 7*(10**(-5))
while V < 0.00018:
    V =V + 1e-7
    # t = ((+(R*T)/((V+b) - b) - (a/((V+b)**2))  -(R*T)/(V - b) - (a/(V**2))))/b
    # if t>0:
    #     maxmin.append(eq(V))
    lst_y.append(eq(V))
    lst_x.append(V)

num = 0
min_y = 10000000000000000000000
max_y = 0
for i in lst_y:
    if i > max_y:
        max_y = i
        max_x = lst_x[num]
    if i < min_y:
        min_y = i
        min_x = lst_x[num]
    num = num + 1


L = 0
V = 7.190000000000005e-05
while V < 0.0001363000000000016:
    V = V + 1e-7
    L = L + math.sqrt((eq(V+(1e-7)) - eq(V))**2 + (1e-7)**2)

plt.plot(lst_x,lst_y)
plt.show()

print(L)


