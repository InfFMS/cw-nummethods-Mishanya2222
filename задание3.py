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
L =0




def eq(V):
    P = (R*T)/(V - b) - (a/(V**2))
    return P





V = 3*(10**(-5))
while V < 0.00018:
    V =V + b
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
V = min_x
while V < max_x:
    V = V + b
    L = L + math.sqrt((-(R*T)/((V+b) - b) - (a/((V+b)**2)))**2 -(R*T)/(V - b) - (a/(V**2)))

plt.plot(lst_x,lst_y)
plt.show()

print(L)



