def solve(n):
    if n<10:
        return "its very cool"
    elif 10<=n<=20:
        return "its cold"
    return "its warm"


temp1,temp2=map(int,input().split())
print(solve(temp1)+","+solve(temp2))
print(f"{(temp1+temp2)/2:.1f}")
print(temp2,temp1)
