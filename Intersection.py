def Intersecion(a,sizeA,b,sizeB):
    I=[]
    i=j=0
    a.sort()
    b.sort()
    while(i<sizeA and j<sizeB):
        #to avoid duplicates
        while(i<sizeA-1 and a[i]==a[i+1]):
            i+=1
        while(j<sizeB-1 and b[j]==b[j+1]):
            j+=1

        if(a[i]<b[j]):
            i+=1
        elif(a[i]>b[j]):
            j+=1
        elif(a[i]==b[j]):
            I.append(a[i]) #or b[j], since both are the same
            i+=1
            j+=1
    print(len(I))
A=[]
n, m=map(int,input().split())
for i in range (0,n):
    na=int(input())
    A.append(na)
B=[]
for i in range (0,m):
    nb=int(input())
    B.append(nb)

Intersecion(A,n,B,m)