def solve(s):
    if len(str(s))==1:
        return s
    else:
        j=0
        while s>0:
            r=s%10
            j+=r
            s//=10
        if len(str(j))!=1:
            return solve(j)
    return j

def is_prime(n):
    if n<2:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        for k in range(3,int(n**0.5)+1):
            if n%k==0:
                return False
    return True

m,n=map(int,input().split())
c=0
num=1
p=[]
while c < max(m,n):
    num+=1
    if is_prime(num):
        c+=1
        p.append(num)
print(solve(p[m-1])*solve(p[n-1]))
    