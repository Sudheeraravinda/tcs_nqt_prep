i=int(input())
u=int(input())
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
for j in range(n):
    if i<=arr[j]-1:
        res=[i ,arr[j]-1]
        print(res, end="")
    i=arr[j]+1
if i<=u:
    print([i,u])

