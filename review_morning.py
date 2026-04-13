n=int(input())
arr=list(map(int,input().split()))
m_l=0
for i in range(n):
    s=0
    for j in range(i,n):
        s+=arr[j]
        if s%2==0:
            l=j-i+1
            if l>m_l:
                m_l=l
        
print(m_l)

            