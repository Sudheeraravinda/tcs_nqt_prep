t=int(input())
for k in range(t):
    n=int(input())
    a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    c=0
    for i in range(n):
        for j in range(n):
            val=str(arr[i])+str(arr[j])
            res=int(val)
            if a<=res<=b:
                c+=1
                
    print(c)