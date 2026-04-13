n=int(input())
if n>30:
    print("Error!!")
    exit()
arr=list(map(int,input().split()))
c=0
s=0
for i in range(n):
    if arr[i]>=10000:
        print("Error!!")
        exit()
        
    if arr[i]%2 != 0:
        s+=arr[i]
        c+=1
print(s,end=" ")
print(c,end=" ")
if c!=0:
    print(f"{s/c:.2f}",end=" ")
else:
    print("0.00",end=" ")
        
