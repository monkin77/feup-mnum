import math

def f(x):
    #return math.sin(x)
    return 1-(math.e ** (-2*x))

def calcAreaTrap(n,h, lb, ub):
    s = (h/2) * (f(lb) + f(ub))
    for i in range(1, n-1, 1):
        s+= 2 * f(h*i) * h/2
    return s

def trap(n, h):
    s = calcAreaTrap(n,h, lb, ub)
    sl = calcAreaTrap(n*2, h, lb, ub)
    sll = calcAreaTrap(n*4, h, lb, ub)
    QC = (sl - s) / (sll - sl)
    print("N=", n, ": \nh: ", h, " S: ", s, " Erro abs: ", s - 2, " QC: ", QC )

def simpson(n,h):
    s1 = somatorio(n, h, 1, 2*n-1, 4)
    s2 = somatorio(n, h, 2, 2*n-2, 2)
    s = (h/3) * (f(0) + f(2*n) + s1 + s2)
    print("N=", n, ": \nh: ", h, " S: ", s, " Erro abs: ", s - 2 )

def somatorio(n, h, start, end, multiplier):
    s = 0
    for i in range(start, end, 2):
        s += f(i*h)
    s *= multiplier
    return s
 

for i in [4,8,16,32,64]:
    lb = 0
    ub = 4
    h = (ub + lb) / (i)
    trap(i,h)
    #simpson(i, h)