'''This is a brute force solution to the maximum contiguous
subarray problem, with a time complexity of O(n²)'''
'''for the optimized algorithm of linear time coplexity,
 kindly refer to kandane.py file'''

def Max_SubArray(arr):
    global_max=0
    for i in range(len(arr)):
        local=0
        for j in range(len(arr)):
            local+=arr[j]
            if(local>global_max):
                global_max=local
    print(global_max) 
A=[]
n=int(input())
for i in range (0,n):
    nbr=int(input())
    A.append(nbr)
Max_SubArray(A)