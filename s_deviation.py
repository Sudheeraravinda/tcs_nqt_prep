import math
n=int(input())
arr=list(map(int,input().split()))
val=0
x = (sum(arr)) / n
for i in range(n):
    val+=(abs((arr[i]-x))**2)
ans=math.sqrt((val)/n)
print(ans)
