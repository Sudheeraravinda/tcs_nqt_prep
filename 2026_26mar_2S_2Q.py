def solve(*args):
    s=sum(args)
    if s==t:
        return s
    else:
        return solve(br[i],2*fl[j])
        

br=list(map(int,input().split(',')))
fl=list(map(int,input().split(',')))
t=int(input())
flag=True
for i in range(len(br)):
    for j in range(len(fl)):
        s=solve(br[i],fl[i])
        if s==t:
            print(s)
            break
        
        