import numpy as np
from sympy import symbols, Eq, solve 
def PowerMethod(A,x,p,k_max):
    #p will be an array of coefficients representing the linear combination
    #of the respective elements
    r = 0 #eigen value
    y = [0]*len(x)
    for i in range(k_max):
        y = A @ x
        print(y)
        r = np.dot(p,y)/np.dot(p,x)
        x = y/np.linalg.norm(y)
    return r,x

p = [2, 1]
A = np.array([[1,2],[-3,-4]])
x = [1,1]
k_max = 4
r,x = PowerMethod(A,x,p,k_max)
print("\nResult: ")
print(r)
print(x)


#init_values is a dictionary of variable:value
def jacobi(init_values, equation):

    return 0

