n=int(input())
d={}
fraud=[]
for i in range(n):
    s,r,amt,ts=input().split()
    #amt=float(amt)
    ts=int(ts)
    k=(s,r,amt)
    if k in d:
        if ts-d[k]<=60:
            fraud.append((s,r,amt,ts))
    d[k]=ts
for j in range(len(fraud)):
    print(*fraud[j])
            
