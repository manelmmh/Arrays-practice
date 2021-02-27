arr=[]
m=int(input())
for i in range(0,m):
    nbr=int(input())
    arr.append(nbr)
print ('The array is', arr)
rev_arr=[]
for i in reversed(range(m)):
    r_nbr=arr[i]
    rev_arr.append(r_nbr)
print('the reversed array is',rev_arr)

