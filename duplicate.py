def findDuplicate(nums):
    temp=0
    nums.sort()
    for i in range(0,len(nums)-1):
        if(nums[i]==nums[i+1]):
            temp=nums[i]
            break
    print(temp)
                     
A=[]
n=int(input())
for i in range (0,n):
    nbr=int(input())
    A.append(nbr)
findDuplicate(A)                   
                    