n=int(input())
n1=n
n2=n
c=0
ans=0
while n1>0:
    r=n1%10
    c+=1
    n1=n1//10
while n2>0:
    r=n2%10
    ans=ans+r**c
    n2=n2//10
if n==ans:
    print("Armstrong number")
else:
    print("Not a Armstrong number")
    