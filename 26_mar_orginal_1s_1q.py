arr=list(map(int,input().split(',')))
p=float('-inf')
for i in range(len(arr)):
    v=1
    for j in range(i,len(arr)):
        v*=arr[j]
        if v>p:
            p=v
print(p)
    
