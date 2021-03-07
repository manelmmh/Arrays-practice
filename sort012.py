
def sort012(arr,n):
    zero=0
    one=0
    two=n-1
    while one<=two:
        if(arr[one]==0):
            arr[zero],arr[one]=arr[one],arr[zero]
            zero+=1
            one+=1
        elif(arr[one]==1):
            one+=1
        else:
            arr[one],arr[two]=arr[two],arr[one]
            two-=1
    return arr
arr=[]
m=int(input())
for i in range(0,m):
    nbr=int(input())
    arr.append(nbr)
print ('The array is', arr)
print('the sorted array is', sort012(arr,m))

        
                