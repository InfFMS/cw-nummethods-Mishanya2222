import numpy
from matplotlib import pyplot as plt
import  math
lst_x = []

lst_y = []
R = 8.31
#[P + a (n2/V2)] (V - nb) = nRT
a = 0.1382
b = 3.19*10**(-5)
T = -130
L =0
dx = 0.01



def eq(V):
    P = -(R*T)/(V - b) - (a/(V**2))
    return P





V = 10**(-5)
while V < 10**(-3):
    V = V + b
    lst_x.append(V)
    lst_y.append(eq(V))


num = 0
min = 10000000000000000000000
max = 0
for i in lst_y:
    num = num + 1
    if i > max:
        max = lst_x[num-1]
    if i < min:
        min = lst_x[num-1]


L = 0
V = min
while V < max:
    V = V + b
    L = L + math.sqrt((-(R*T)/((V+b) - b) - (a/((V+b)**2)))**2 - -(R*T)/(V - b) - (a/(V**2)))



print(L)


