s=input()
s1=s.lower()
d={}
flag=True
for i in s1:
    d[i]=d.get(i,0)+1
for j in d:
    if d[j]==1:
        flag=False
        print(j)
        break
if flag:
    print(None)
print(max(d,key=d.get))
