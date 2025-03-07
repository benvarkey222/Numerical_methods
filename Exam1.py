import numpy as np

#Problem 4

p2_fxn = lambda x: ((np.sqrt(2)/2)*(4*x/np.pi)*((-4*x/np.pi)+2)) + ((2*x/np.pi)*((4*x/np.pi)-1))
p3_fxn = lambda x: (np.sqrt(2)/2)+((np.sqrt(2)/2)*(x-(np.pi / 4)))-((np.sqrt(2)/4)*(x-(np.pi / 4))**2)
actual = np.sin(np.pi/3)
print("Problem 4: ")
print("\nInterpolation Abs Error: ", np.abs(actual -p2_fxn(np.pi/3)))
print("\nTaylor Poly Abs Error: ", np.abs(actual -p3_fxn(np.pi/3)))

#Problem 6
print("\nProblem 6 calculations:  ")
next_x = lambda y,z: 1/8 *(1+y-2*z)
next_y =lambda  x,z: 1/8*(2 - 5*x -z)
next_z = lambda x: 1/8 * (3+4*x)

print("\nFirst Iteration: ")
x_1 = next_x(0,0)
y_1 = next_y(x_1,0)
z_1 = next_z(x_1)

print(x_1)
print(y_1)
print(z_1)
print("\nSecond Iteration: ")
x_2 = next_x(y_1,z_1)
y_2 = next_y(x_2,z_1)
z_2 = next_z(x_2)

print(x_2)
print(y_2)
print(z_2)

#Problem 7
#Eaach of the parameters are vectors
def TriDiag(a,c,d,b):
    n = len(d)
    x = [0]*n
    #forward elim
    for i in range(1,n):
        d_i = d[i]
        mult = a[i-1]/d[i-1]
        d[i] = d_i - (mult*c[i-1])
        b[i]= b[i] - (mult*b[i-1])
    #backward sub
    x[n-1] = b[n-1]/d[n-1]
    for i in range(n-2,-1,-1):
        c_i = c[i]
        x[i] = (b[i] - (c_i*x[i+1]))/d[i]
    return [float(y) for y in x]






n = 100
d = np.full(n, 3.0)         # Main diagonal
c = np.full(n-1, 3/2)      # Superdiagonal
a = np.full(n-1, -1/2)  
b = [2]*n
# print("A: ", A)
# print("b: ", b)
# new_b =UpperTri(A)
# print("A: ", A)
# print("b: ", new_b)

# x = BackwardSub(A,new_b)

x = TriDiag(a,c,d,b)
print("\nProblem 7 Solution:\n")
print(x)

