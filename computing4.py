


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






matrix = [[10,2,-1],[-3,-5,2],[1,1,6]]
b = [27,-61.5,-21.5]
lower = Triangulate(matrix,b)
print(matrix[0])
print(matrix[1])
print(matrix[2])
print("\n\n")
print(lower[0])
print(lower[1])
print(lower[2])
print("\n\n")
print(b)
