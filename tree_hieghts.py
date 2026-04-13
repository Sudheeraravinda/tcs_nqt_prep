a,b,c,d=map(int,input().split())
if (a<0 or b<0 or c<0 or d<0):
    print("Not valid inputs")
    exit()
l=[a,b,c,d]
arr=[]
for i in range(4):
    for j in range(i+1,4):
        v=abs(l[i]-l[j])
        if v in arr:
            print(v)
            exit()
        else:
            arr.append(v)
print(None)
        
        
    