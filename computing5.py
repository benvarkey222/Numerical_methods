import numpy as np
def PowerMethod(A,x,p,k_max):
    #p will be an array of coefficients representing the linear combination
    #of the respective elements
    r = 0 #eigen value
    y = [0]*len(x)
    for i in range(k_max):
        y = A @ x
        r = np.dot(p,y)/np.dot(p,x)
        x = y/np.linalg.norm(y)
    return r,x



#init_values is a dictionary of variable:value
def jacobi(init_values, A,b,max=10000):
    n = len(A[0])
    sol = [0]*n
    guess= init_values
    i = 0
    while(not np.allclose(A @ guess, b, atol=1e-6) and i < max ):
        for row in range(0,n): #goes down a row
            diag = A[row][row]
            if row == 0:
                # sol[row] = (b[row] - (A[row][row+1]*guess[row+1]))/diag
                sol[row]  = (b[row] - sum([guess[i] * A[row][i] for i in range (row +1, n)]))/diag
            elif row == n-1:
                # sol[row] = (b[row]- (A[row][row-1]*guess[row-1]))/diag
                sol[row]  = (b[row] - sum([guess[i] * A[row][i] for i in range (0, row)]))/diag
            else:
                left = sum([guess[i] * A[row][i] for i in range (0, row)])
                right = sum([guess[i] * A[row][i] for i in range (row +1, n)])
                # sol[row] = (b[row]-(guess[row-1]* left) - (guess[row+1]* right))/diag
                sol[row] = (b[row]- left - right)/diag
            i =i+1
        guess = sol

    # print(A @ sol - b)
    return [float(x) for x in sol], i

def GaussS(init_values, A,b,max=10000):
    n = len(A[0])
    sol = init_values
    i = 0
    while(not np.allclose(A @ sol, b, atol=1e-6) and i < max):
        for row in range(0,n): #goes down a row
            diag = A[row][row]
            if row == 0:
                # sol[row] = (b[row] - (A[row][row+1]*guess[row+1]))/diag
                sol[row]  = (b[row] - sum([sol[i] * A[row][i] for i in range (row +1, n)]))/diag
            elif row == n-1:
                # sol[row] = (b[row]- (A[row][row-1]*guess[row-1]))/diag
                sol[row]  = (b[row] - sum([sol[i] * A[row][i] for i in range (0, row)]))/diag
            else:
                left = sum([sol[i] * A[row][i] for i in range (0, row)])
                right = sum([sol[i] * A[row][i] for i in range (row +1, n)])
                # sol[row] = (b[row]-(guess[row-1]* left) - (guess[row+1]* right))/diag
                sol[row] = (b[row]- left - right)/diag
            i = i+1

    # print(A @ sol - b)
    return [float(x) for x in sol], i

def make(n):
    A = np.diag(np.full(n, 3)) + np.diag(np.full(n-1, -1),k=1) + np.diag(np.full(n-1,-1), k=-1)
    b= [3/2]*n
    A = A.astype(float)
    for i in range(n):
        if not(A[(n-i)-1][i] == 3 or A[(n-i)-1][i] == -1):
            A[(n-i)-1][i] = 1/2
        if i == 0 or i == n-1:
            b[i] = 5/2
        if i == n//2:
            b[i] = 1
    
    return A,b


#Problem 1: Power Method
p = [2, 1]
A = np.array([[1,2],[-3,-4]])
x = [1,1]
k_max = 4
r,x = PowerMethod(A,x,p,k_max)
print("\nProblem 1 Results: ")
print("Dominant Eigenvalue: ", r)
print("Dominant Eigenvector: ", x)


#Problem 2: Jacobi
n = 50
main_diag = np.full(n, 10)         # Main diagonal
upper_diag = np.full(n-1, -2)      # Superdiagonal
lower_diag = np.full(n-1, 4)  
A = np.diag(main_diag) + np.diag(upper_diag, k=1) + np.diag(lower_diag, k=-1)
init_values = [0]*50
b = [(101*i)%25 for i in range(1, 51)]
sol = jacobi(init_values,A,b)
print("\n Problem 2 Solution: ", sol)


#Problem 3: Gauss
init_values = [0]*6
A2 = np.array([[-12,6,0,0,-1,1],[-12,18,0,1,0,0],[1,1,7,-1,-1,1],[10,-3,0,-21,0,0],[3,6,3,0,15,1],[0,0,0,0,-1,-19]])
b2 = [11,-1,-20,6,5,9]
sol2 = GaussS(init_values,A2,b2)
print("\n Problem 3 Solution: ", sol2)


#Problem 4: Both
dims = [5, 7, 9, 11, 13]
print("\n Problem 4 Solution: ")
for d in dims:
    A3,b3 = make(d)
    j_sol, j_i = jacobi([0]*d,A3, b3)
    g_sol, g_i= GaussS([0]*d,A3, b3)
    print("Dim: ", d, " Jacobi Iterations: ", j_i, "Gauss Iterations: ", g_i)
    print("Jacobi Sol: ", j_sol)
    print("Gauss Sol: ", g_sol)
    print("\n")







