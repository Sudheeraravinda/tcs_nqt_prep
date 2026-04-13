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
p=[]
num=1
while c<(m+n):
    num+=1
    if is_prime(num):
        c+=1
        p.append(num)
print(sum(p[m-1:m+n]))
        
