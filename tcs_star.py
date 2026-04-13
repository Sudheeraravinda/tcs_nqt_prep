def palin(i):
    t=i
    ans = 0
    while i > 0:
        r = i % 10
        ans = ans * 10 + r
        i = i//10
    if ans == t:
        return False
    return True
    

a = int(input())
b = int(input())
flag=True
for i in range(a,b+1):
    if (i%7) == 0 and (i%5) !=0 and palin(i):
        print(i, end = " ")
        flag=False
if flag:
    print(-1)
        
             
        
        