#We can use the sort() built-in function in python 
arr=[]
m=int(input()) #size of the array
for i in range(0,m):
    arr.append(int(input()))
print(arr)
arr.sort()
k=int(input())
print(str(k)+'th smallest element is', arr[k-1])
print(str(k)+'th largest element is', arr[-k])
