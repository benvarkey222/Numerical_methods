import numpy as np

def SplineCoeff(t, y):
    n = len(t) - 1
    z= [0.0] * (n+1)
    h = [0.0] * n
    b = [0.0] * n
    u = [0.0] * n
    v = [0.0] * n
    for i in range(n):
        h[i] = t[i + 1] - t[i]
        b[i] = (y[i + 1] - y[i]) / h[i]
    u[1] = 2*(h[0] + h[1])
    v[1] = 6 * (b[1] - b[0])
    for i in range(2, n):
        u[i] = 2 * (h[i] + h[i - 1]) - (h[i-1] ** 2) / u[i - 1]
        v[i] = 6 * (b[i] - b[i-1]) - (h[i-1] * v[i - 1]) / u[i - 1]
    z[n] = 0

    for i in range(n - 1, 0, -1):
        z[i] = (v[i] - h[i] * z[i + 1]) / u[i]
    
    z[0]= 0
    return z


def SplineEval(x,y,z,t):
    n = len(x) - 1
    j = 0
    for i in range(n-1, -1, -1):
        if t - x[i]>=0:
            j = i
            break
    
    h = x[j + 1] - x[j]
    S = (z[j]/2.0)+ (t-x[j])*(z[j+1] - z[j])/(6.0*h)
    S = -(h/6.0)*(z[j+1]+2*z[j])+((y[j+1] - y[j])/h) + (t-x[j])*S
    return y[j] + (t-x[j])*S




# x = [-1.0, 0.0, 1.0]
# y = [1.0,2.0,-1.0] 
# z = SplineCoeff(x, y)
# print(z)
# print(SplineEval(0, y, z, x))



def ParametricSpline_Coeff(t, x, y):
    z1 = SplineCoeff(t, x)
    z2 = SplineCoeff(t, y)
    return(z1, z2)

def ParametricSpline_Eval(t, x, y, z1, z2, T):
    r = [0.0]* len(T)
    for  i in range(len(T)):
        r[i] = SplineEval(t,x,z1,T[i]), SplineEval(t,y,z2,T[i])
    return r

t = [.05*i for i in range(200)]
x = [3*np.sin(t[i]*np.pi/2.0) for i in range(len(t))]
y = [5*np.log(t[i]+1)*np.cos(np.pi*t[i]/3.0) for i in range(len(t))]
z1, z2 = ParametricSpline_Coeff(t, x, y)
T = [.01*i for i in range(1000)]
print(ParametricSpline_Eval(t, x, y, z1, z2, T))


