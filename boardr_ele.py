m,n=map(int,input().split())
if m<=0 or n<=0:
    print("invalid input")
    exit()
matrix=[]
for i in range(m):
    r=list(map(int,input().split()))
    if len(r)!=n:
        print("invalid input")
        exit()
    matrix.append(r)
s=0
for i in range(m):
    for j in range(n):
        if (i==0 or i==m-1) or (j==0 or j==n-1):
            s+=matrix[i][j]
            print(matrix[i][j],end=" ")
print()
print(s)