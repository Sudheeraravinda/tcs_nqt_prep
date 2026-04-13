arr=list(map(int,input().split()))
f=float('+inf')
s=float('+inf')
for i in range(len(arr)):
    if arr[i]<f:
        s=f
        f=arr[i]
    if arr[i]!=f and arr[i]<s:
        s=arr[i]
print(s)
