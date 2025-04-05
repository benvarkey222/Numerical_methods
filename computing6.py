import numpy as np

#data = list of tuples (x,y)
def Lagrange(data, t):
    n = len(data)
    result = 0
    for i in range(n):
        l = 1
        for j  in range(n):
            if j != i:
                l = l* (t-data[j][0])/(data[i][0]-data[j][0])
        result = result + (data[i][1]*l)
    return result



def DividedDifferences_Coeff(data):
    n = len(data)
    a = [data[i][1] for i in range(n)]
    x = [data[i][0] for i in range(n)]
    f= [data[i][1] for i in range(n)]
    for aIndx in range(1,n):
        # print(f)
        for fIndx in range(aIndx, n):
            a[fIndx] = (f[fIndx] - f[fIndx-1])/(x[fIndx] - x[fIndx-aIndx])
        f[aIndx:n] = a[aIndx:n]
    return a

def DividedDifferences_Eval(a, t, x):
    ans = a[0]
    n = len(a)
    for i in range(n-1):
        prod = a[i+1]
        for xIndex in range(0,i+1):
            prod= prod*(t - x[xIndex])
        ans = ans + prod
    return ans







# #Lagrange
data1= [(-31,-2),(-5,-1),(1,1),(11,2),(61,3)]
t = 0
print("Lagrange: ", Lagrange(data1,t))
#DD
a= DividedDifferences_Coeff(data1)
x = [data1[i][0] for i in range(len(data1))]
print("Divided Differences: ", DividedDifferences_Eval(a,t,x))


# data2= [(.25,-2),(.125,-3),(.0625,-4)]
# a= DividedDifferences_Coeff(data2)

# t = .0625
# x = [data2[i][0] for i in range(len(data2))]
# print(DividedDifferences_Eval(a,t,x))
# #Lagrange
# data2= [(.25,-2),(.125,-3),(.0625,-4)]
# t = .1854
# print("Lagrange: ", Lagrange(data2,t))
# #DD
# a= DividedDifferences_Coeff(data2)
# x = [data2[i][0] for i in range(len(data2))]
# print("Divided Differences: ", DividedDifferences_Eval(a,t,x))