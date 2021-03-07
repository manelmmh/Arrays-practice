#since the order doesn't matter, we only swap elements as follows
def neg_pos_sort(A):
    j=0
    for i in range(0,len(A)):
        if(A[i]<0):
            temp=A[i]
            A[i]=A[j]
            A[j]=temp
            j+=1
    return A

A=[]
n=int(input())
for i in range (0,n):
    nbr=int(input())
    A.append(nbr)
print('the array before sorting: ', A)
print('after sorting: ',neg_pos_sort(A))

