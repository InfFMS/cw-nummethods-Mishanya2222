import numpy
from matplotlib import pyplot as plt
import  math
lst_x = []
lst_y = []

R = 8.31
#[P + a (n2/V2)] (V - nb) = nRT
a = 0.1382
b = 3.19*10**(-5)
T = -133
maxmin = []
def eq(V):
    P = -(R*T)/(V - b) - (a/(V**2))
    return P


V = 2.15*(10**(-5))
while V < 0.0004:
    V =V + b
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

print(min_x,max_x)

plt.plot(lst_x,lst_y)
plt.show()





