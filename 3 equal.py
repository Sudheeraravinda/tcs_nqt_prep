def func(a,b,c):
    ct+=1
    if a==b==c:
        return ct
    else:
        return func(a-1,b-1,c+1)

#n=int(input())
a,b,c=map(int,input().split())
ct = 0
if a==b==c:
    print(0)
else:
    print(func(a,b,c))
    