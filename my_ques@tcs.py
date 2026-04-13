def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    else:
        for i in range(3,int(n**0.5)+1):
            if n%i == 0:
                return False
    return True

def nth_prime(n):
    c=0
    num=1
    while c<n:
        num+=1
        if is_prime(num):
            c+=1
    return num

x,y = map(int,input().split())
ans= nth_prime(x)*nth_prime(y)
print(ans-1)