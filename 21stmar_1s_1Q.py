n=int(input())
ans=0
if n<1000:
    ans=n-(n/20)
elif n<5000:
    ans=n-(n/10)
else:
    ans=n-((15*n)/100)
print(ans)