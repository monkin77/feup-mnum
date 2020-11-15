import math

def dydx(x,y,z):
    return z*y + x

def dzdx(x,y,z):
    return z*x +y

lb = 0
ub = 0.5
pi = (0,1,1)
h = 0.05

def SolveByEuler(lb, ub, h, pi):
    qc = 100
    #while( abs(qc) - 2 > 0.5 ):
    s = Euler(lb, ub, h, pi)
    #sl = Euler(lb, ub, h/2, pi)
    #sll = Euler(lb, ub, h/4, pi)

            
def Euler(lb, ub, h, pi):
    nextX = lb
    nextY = pi[1]
    nextZ = pi[2]
    i = lb
    while(i < ub):
        x = nextX
        y = nextY
        z = nextZ
        nextX = x + h
        nextY = y + dydx(x, y, z) * h
        nextZ = z + dzdx(x,y,z) * h
        if( (nextX == 0.1) or (nextX == 0.5) ):
            print(nextX, nextY, nextZ)
        i += h
        print(i)
    return (nextX, nextY, nextZ)

SolveByEuler(lb,ub,h,pi)
