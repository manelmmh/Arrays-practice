#another approach to solving the negative, positive numbers sorting 
# is by using 2 index pointers, one is incremented and the other is decremented

    

def partition(lo,hi):
    up_ptr=lo
    dwn_ptr=hi
    while(up_ptr<dwn_ptr):
        while(A[up_ptr]<0):
            up_ptr+=1
        while(A[dwn_ptr]>0):
            dwn_ptr-=1
        if(up_ptr<dwn_ptr):
            A[up_ptr], A[dwn_ptr]=A[dwn_ptr], A[up_ptr]

A=[]
n=int(input())
for i in range (0,n):
    nbr=int(input())
    A.append(nbr)
print('the array before sorting: ', A)
partition(0,n-1)
print('after sorting: ', A)