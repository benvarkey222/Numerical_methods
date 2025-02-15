


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





matrix = [[1,0,1/3,0],[0,1,3,-1],[3,-3,0,6],[0,2,4,-6]]
# b = [27,-61.5,-21.5]
lower = Triangulate(matrix)
print(matrix)
print("\n\n")
print(lower)


