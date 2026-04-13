m,n=map(int,input().split())
matrix=[]
for i in range(m):
    r=list(map(int,input().split()))
    if len(r)!=n:
        print("Error!! Invalid Input")
        exit()
    matrix.append(r)
    
for i in range(m):
    if i%2==0:
        for j in range(n):
            print(matrix[i][j],end="")
    else:
        for j in range(n-1,-1,-1):
            print(matrix[i][j],end="")