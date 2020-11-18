import math

def dvdt(t,v,a):
    return a

def dadt(t,v,a):
    return 0.5*a - v

def Solve(lb, ub, h, pi):
    sol = rk2(lb,ub,h,pi)
    sols = rk2(lb,ub,h/2,pi)
    solss = rk2(lb,ub,h/4, pi)

    qcV = (sols[1] - sol[1]) / (solss[1] - sols[1])
    errV = (solss[1] - sols[1]) / ((2**2) - 1)

    qcA = (sols[2] - sol[2]) / (solss[2] - sols[2]) 
    errA = (solss[2] - sols[2]) / ((2**2) - 1)

    print(sol, sols, solss)
    print("qcV: ", qcV, " errV: ", errV)
    print("qcA: ", qcA, " errA: ", errA)

def rk2(lb,ub,h,pi):
    t = pi[0]
    v = pi[1]
    a = pi[2]
    while(round(t,20) < ub):        # need to round to 20 because of precision
        delta1V = h * dvdt(t,v,a)
        delta1A = h * dadt(t,v,a)
        delta2V = h * dvdt(t+h/2, v+delta1V/2, a + delta1A/2)
        delta2A = h * dadt(t+h/2, v+delta1V/2, a + delta1A/2)
        t += h
        v += delta2V
        a += delta2A
        print(t,v,a)
    return (t,v,a)

lb = 0
ub = 4
pi = (0,2,0)
h = 0.01

Solve(lb,ub,h,pi)
