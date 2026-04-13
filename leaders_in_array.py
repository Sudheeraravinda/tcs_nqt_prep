
arr=list(map(int,input().split()))
n=len(arr)
ans=[arr[n-1]]
v=arr[n-1]
for i in range(n-2,-1,-1):
    if arr[i]>v:
        ans.append(arr[i])
        v=arr[i]
ans.reverse()
print(*ans)