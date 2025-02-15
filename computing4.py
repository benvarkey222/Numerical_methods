


#Problem 1
#changes matrix to be upper tri and returns the lower tri
def Triangulate(matrix, b):
    #check if n by n and if b dimesions line up
    lower = [[1,0,0],[0,1,0],[0,0,1]]
    for col in range(len(matrix[0])):
        for row in range(col+1, len(matrix)):
            mult = matrix[row][col]/matrix[col][col]
            for rIndex in range(col, len(matrix[0])):
                matrix[row][rIndex] = matrix[row][rIndex] - mult*matrix[col][rIndex]
            b[row] = b[row] - mult*b[col]
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










matrix = [[10,2,-1],[-3,-5,2],[1,1,6]]
b = [27,-61.5,-21.5]
b2 = [27,-61.5,-21.5]
lower = Triangulate(matrix,b)
sol = BackwardSub(matrix, b)
sol2 = FowardSub(lower,b2)
print(sol)
print(sol2)

