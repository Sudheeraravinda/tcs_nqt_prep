def min_swaps(s,x):
    if sorted(s)!=sorted(x):
        return -1
    pos={}
    for i in range(len(x)):
        pos[x[i]]=i
    arr=[]
    for j in range(len(s)):
        arr.append(pos[s[j]])
    swaps=0
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                swaps+=1
    return swaps

s=list(map(int,input().split()))
x=list(map(int,input().split()))
print(min_swaps(s,x))
