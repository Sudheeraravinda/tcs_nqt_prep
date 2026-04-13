n=int(input())
arr=list(map(int,input().split()))
val=float('-inf')
ans=[]
for i in range(n):
    for j in range(i+1,n):
        if arr[i]*arr[j]>val:
            val=arr[i]*arr[j]
            ans=[arr[i],arr[j]]
print(val)
print(ans)
