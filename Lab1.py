import numpy as np

def FowardElim(A,b):
    n= len(A)
    l = list(range(n)) #row indexes
    for colIndex in range(n):
        max= np.abs(A[l[colIndex]][colIndex])
        swappedLIndex = colIndex
        # print(colIndex)
        for lIndex in range(colIndex+1, n):
            #find the the greatest entry in the rows which 
            #havent been used for pivots
            rIndex=l[lIndex]
            if np.abs(A[rIndex][colIndex])>max:
                max = np.abs(A[rIndex][colIndex])
                swappedLIndex = lIndex
        #max has been found. now swap entrys in l at colIndex with 
        #entry at maxIndex
        temp = l[colIndex]
        l[colIndex] = l[swappedLIndex]
        l[swappedLIndex] = temp
        #apply row operation to all rows below the l[colIndex]
        #l[colIndex] = pivot index
        for lIndex in range(colIndex+1,n):
            # print(l)
            # print(A[l[lIndex]][colIndex], "/", A[l[colIndex]][colIndex])
            xmult = A[l[lIndex]][colIndex]/A[l[colIndex]][colIndex]
            for curRowIndex in range(colIndex,n):
                # print("Row: ", l[lIndex]+1, " - ",xmult, " * Row: ",l[colIndex]+1 )
                A[l[lIndex]][curRowIndex] = A[l[lIndex]][curRowIndex] - (xmult*A[l[colIndex]][curRowIndex])
                # print("result: ",  A[l[lIndex]][curRowIndex])
            b[l[lIndex]] = b[l[lIndex]] - (xmult*b[l[colIndex]])
    #return new A and B in proper order 
    newA = [0]*n
    newB = [0]*n
    for lIndex in range(n):
        index = l[lIndex]
        newA[lIndex] = A[index]
        newB[lIndex] = b[index]

    return newA, newB



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

def printM(A,b):
    str = ""
    for i in range(len(A)):
        print(A[i])
    print("b = ", b)
            
matrix= [[2,2,1],[1,1,1],[3,2,1]]
b = [27,-61.5,-21.5]
print("\nTestcase 1:\n ")
printM(matrix,b)
print("\nAfter:\n ")
A,new_b =FowardElim(matrix,b)
printM(A,new_b)
x = BackwardSub(A,new_b)
print("sol = ", x)
matrix= [[10,2,-1],[-3,-5,2],[1,1,6]]
b = [27,-61.5,-21.5]
print("\nTestcase 2:\n ")
printM(matrix,b)
print("\nAfter:\n ")
A,new_b =FowardElim(matrix,b)
printM(A,new_b)
x = BackwardSub(A,new_b)
print("sol = ", x)
matrix= [[5,7,6,5],[7,10,8,7],[6,8,10,9],[7,7,9,10]]
b = [17,83.1,28,9]
print("\nTestcase 3:\n ")
printM(matrix,b)
print("\nAfter:\n ")
A,new_b =FowardElim(matrix,b)
printM(A,new_b)
x = BackwardSub(A,new_b)
print("sol = ", x)
matrix= [[5,7,6,5],[7,10,8,7],[6,8,10,9],[7,7,9,10]]
b = [19.28,37.29,123.21,12.293]
print("\nTestcase 4:\n ")
printM(matrix,b)
print("\nAfter:\n ")
A,new_b =FowardElim(matrix,b)
printM(A,new_b)
x = BackwardSub(A,new_b)
print("sol = ", x)

