
import numpy as np

#Problem 1
#changes matrix to be upper tri and returns the lower tri
def Triangulate(matrix):
    #check if n by n and if b dimesions line up
    lower = []
    for i in range(len(matrix)):
        row = [0]*len(matrix)
        row[i] = 1
        lower.append(row)
    
    for col in range(len(matrix[0])):
        for row in range(col+1, len(matrix)):
            mult = matrix[row][col]/matrix[col][col]
            for rIndex in range(col, len(matrix[0])):
                matrix[row][rIndex] = matrix[row][rIndex] - mult*matrix[col][rIndex]
            #b[row] = b[row] - mult*b[col]
            lower[row][col] = mult
    return lower

#to solve Ux = b
def BackwardSub(U,b):
    n= len(U)
    x =[0]*n
    
    x[n-1] = b[n-1]/U[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = b[i]
        for j in range(i+1,n):
            x[i] = x[i] - (U[i][j]*x[j])
        x[i] = x[i]/U[i][i]
    return x

def FowardSub(L,b):
    n= len(L)
    x =[0]*n
    
    x[0] = b[0]/L[0][0]
    for i in range(1,n):
        x[i] = b[i]
        for j in range(0,i):
            x[i] = x[i] - (L[i][j]*x[j])
        x[i] = x[i]/L[i][i]
    return x

def LUSolve(A, b):
    lower=Triangulate(A,b)
    y = FowardSub(lower, b)
    print(y)
    return BackwardSub(A,y)

def Gauss(matrix, b):
    lower = [[1,0,0],[0,1,0],[0,0,1]]
    for col in range(len(matrix[0])):
        for row in range(col+1, len(matrix)):
            mult = matrix[row][col]/matrix[col][col]
            for rIndex in range(col, len(matrix[0])):
                matrix[row][rIndex] = matrix[row][rIndex] - mult*matrix[col][rIndex]
            b[row] = b[row] - mult*b[col]
            lower[row][col] = mult
    return BackwardSub(matrix,b)


def Doolittle(A, uD, lD):
    #intialize U and L as emtry matices 
    #enters diagionals for each one
    #for 0 to uD or lD length (k)
        #check whether entry is defined in uD or aD
        #if defined in uD
            #for k+1 to uD length (i)
                #define (a) entry in k column
                #for 1 to k-1 (m)
                    #subtract (entries in l i row * entries in u k col) from 
                    # entries in k column of a 
                #divind by uD entry
                #add entry to l ik entry
        #else if defined in lD
            #for k+1 to uD length (j)
                #define (a) entry in k row
                #for 1 to k-1 (m)
                    #subtract (entries in l k row * entries in u j col) from 
                    # entries in k column of a 
                #divind by lD entry
                #add entry to U kj entry
    n = len(uD)
    U = np.zeros((n,n))
    L = np.zeros((n,n))

    
    #intialize U and L as emtry matices 
    #enters diagionals for each one
    for i in range(n):
        U[i,i] = uD[i]
        L[i,i] = lD[i]
    
    for k in range(n):
        if U[k,k]!=0: #defined in uD
            for i in range(k, n):
                l_entry = A[i,k]
                for m in range(0, k): #check indices
                    #l_entry = l_entry - L[i]@U[:k]
                    l_entry= l_entry - (L[i,m]*U[m,k])
                l_entry = l_entry/U[k,k]
                L[i,k] = l_entry
            for j in range(k+1, n):
                u_entry = A[k,j]
                for m in range(0, k): #check indices
                    #u_entry = u_entry - L[k]@U[:j]
                    u_entry = u_entry - (L[k,m]*U[m,j])
                u_entry = u_entry/L[k,k]
                U[k,j] = u_entry        
        elif L[k,k] != 0 : #defined in lD
            for j in range(k, n):
                u_entry = A[k,j]
                for m in range(0, k): #check indices
                    #u_entry = u_entry - L[k]@U[:j]
                    u_entry= u_entry - (L[k,m]*U[m,j])
                u_entry = u_entry/L[k,k]
                U[k,j] = u_entry
            for i in range(k+1, n):
                l_entry = A[i,k]
                for m in range(0, k): #check indices
                    #l_entry = l_entry - L[i]@U[:k]
                    l_entry= l_entry - (L[i,m]*U[m,k])
                l_entry = l_entry/U[k,k]
                L[i,k] = l_entry    
    return L,U

def matrix_mult(A, B):
    product = 0
    if len(A[0]) == len(B): #if As column number = Bs row number
        product  = np.zeros((len(A), len(B[0])))
        (rnum,cnum) = product.shape
        for r in range(rnum):
            for c in range(cnum):
                row_A = A[r, :]  # Row 2 of matrix A (indexing starts at 0)
                col_B = B[:, c]
                product[r,c] = sum(row_A*col_B)
    return product


matrix = np.array([[5,7,6,5],[7,10,8,7],[6,8,10,9],[5,7,9,10]])
lD = [0,0,7,9]
uD = [3,5, 0, 0]
L,U = Doolittle(matrix,uD,lD)
print("L:", L)
print("U: ", U)
print(matrix_mult(L,U))


# matrix = [[1,0,1/3,0],[0,1,3,-1],[3,-3,0,6],[0,2,4,-6]]
# # b = [27,-61.5,-21.5]
# lower = Triangulate(matrix)
# print(matrix)
# print("\n\n")
# print(lower)


