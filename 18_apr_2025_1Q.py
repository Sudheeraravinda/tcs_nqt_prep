
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
if m<=0 or n<=0:
    print("Wrong input")
    exit()
arr=[]
for i in range(m):
    r=list(map(int,input().split()))
    if len(r)!=n or any(x<0 for x in r):
        print("Wrong Input")
        exit()
    arr.append(r)
        
for i in range(m):
    f=True
    for j in range(n):
        if is_prime(arr[i][j]):
            f=False
            break
    if f:
        print("Invalid")
        exit()
        
print("Valid")
            
            

    
    

            

            