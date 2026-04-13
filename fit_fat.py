t=int(input())
for k in range(t):
    r=int(input())
    a=[]
    for i in range(r):
        l=list(map(int,input().split()))
        a.append(l)
    if (r*3)%2==0:
        print("Fat")
    else:
        print("Fit")