def rotate( arr, n):
    arr[:0]=[arr[n-1]]
    arr.pop(n)
    
A=[]
n=int(input())
for i in range (0,n):
    nbr=int(input())
    A.append(nbr)
rotate(A,A[n-1])