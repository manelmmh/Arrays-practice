def kadane(arr):
    local=0
    global_max=float('-inf')
    for i in range(0,len(arr)):
        local=max(arr[i],arr[i]+local)
        if(local>global_max):
            global_max=local
    return global_max
A=[]
n=int(input())
for i in range (0,n):
    nbr=int(input())
    A.append(nbr)
kadane(A)