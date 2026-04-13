n=int(input())
arr=list(map(int,input().split()))
t=int(input())
ans=[]
for i in range(n):
    s=0
    v=[]
    for j in range(i,n):
        v.append(arr[j])
        s+=arr[j]
        if s==t:
            ans.append(v.copy())
print(ans)
            