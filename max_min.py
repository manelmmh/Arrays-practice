
A=[]
m=int(input())
for i in range(0,m):
    nbr=int(input())
    A.append(nbr)
print('The array is', A)
mx=mn=A[0]
for i in range(0,m):
    if(A[i]>mx):
        mx=A[i]
    elif (A[i]<mn):
         mn=A[i]
print('maximum: ', mx)
print('minimum: ', mn)
