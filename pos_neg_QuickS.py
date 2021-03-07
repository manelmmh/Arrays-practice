#another approach to solving the negative, positive numbers sorting 
# is by using quicksort, the result will also be sorted
#in ascending order
'''def quickS(lo,hi):
    if(lo<hi):
        pivot=partition(lo,hi+1)
        quickS(lo,pivot-1)
        quickS(pivot+1,hi) '''
    

def partition(lo,hi):
    #pivot=A[lo]
    up_ptr=lo
    dwn_ptr=hi
    while(up_ptr<dwn_ptr):
        while(A[up_ptr]<0):
            up_ptr+=1
        while(A[dwn_ptr]>0):
            dwn_ptr-=1
        if(up_ptr<dwn_ptr):
            A[up_ptr], A[dwn_ptr]=A[dwn_ptr], A[up_ptr]
    '''A[lo]= A[dwn_ptr]
    A[dwn_ptr]=pivot
    return dwn_ptr'''
A=[]
n=int(input())
for i in range (0,n):
    nbr=int(input())
    A.append(nbr)
print('the array before sorting: ', A)
partition(0,n-1)
print('after sorting: ', A)