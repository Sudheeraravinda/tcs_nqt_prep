n=int(input())
arr=list(map(int,input().split()))
flag=True
s=0
t=sum(arr)
for i in range(n):
    t=t-arr[i]
    if t==s:
        flag=False
        print(i)
    s+=arr[i]
if flag:
    print(-1)