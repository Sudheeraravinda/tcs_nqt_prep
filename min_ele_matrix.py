m,n=map(int,input().split())
if m<=0 or n<=0:
    print("invalid input")
    exit()
matrix=[]
low=float('+inf')
for i in range(m):
    r=list(map(int,input().split()))
    if len(r)!=n:
        print("invalid input")
        exit()
    matrix.append(r)
    s=min(r)
    if s<low:
        low=s
    
print(low)
print(matrix)