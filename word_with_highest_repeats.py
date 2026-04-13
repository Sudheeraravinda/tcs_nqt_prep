s=input()
arr=s.split()
m=0
ans=""
for i in range(len(arr)):
    d={}
    n=arr[i]
    for j in range(len(n)):
        d[n[j]]=d.get(n[j],0) + 1
    rm=max(d.values())
    if rm>m:
        m=rm
    ans=n
print(ans)
                      