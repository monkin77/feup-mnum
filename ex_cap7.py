import math
import time

def f(x,y):
    return math.sin(x/2) + (x**2) - math.cos(y)

def dfdx(x,y):
    return 0.5 * math.cos(x/2) + 2*x 

def dfdy(x,y):
    return math.sin(y)

def invert_hess(x,y):
    return [  (1 / (2 - (math.sin(x/2)/4)), 0 ), (0, 1/math.cos(y)) ]

def LM(x, y, tolerance, lamb, isMin):             # Método Levemberg and Marquardt
    while(1):
        invertHess = invert_hess(x,y)
        gradX = dfdx(x,y)
        gradY = dfdy(x,y)
        nextX = x - ( ( invertHess[0][0] * gradX + invertHess[0][1] * gradY) + ( lamb * gradX )  )
        nextY = y - ( ( invertHess[1][0] * gradX + invertHess[1][1] * gradY ) + ( lamb * gradY ) )

        #if((round(abs(nextX - x), 3) <= tolerance) and ( round(abs(nextY - y), 3) <= tolerance)):
        #    break

        func = f(x, y)
        nextFunc = f(nextX, nextY)
        print(x, y, nextX, nextY, nextFunc)
        
        if( abs(round(nextFunc - func, 3)) <= tolerance ):
            break

        if(nextFunc > func):
            lamb *= 2
        else:
            lamb /= 2
            x = nextX
            y = nextY
        
        time.sleep(1)
    return nextFunc
    

x0 = -10
y0 = -1
tolerance = 0.001   
lamb = 0.01     #lambda
min = LM(x0, y0, tolerance, lamb, True)
print("Min is: ", min)
