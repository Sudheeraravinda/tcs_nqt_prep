num = int(input())
s=0
while num > 0:
    rem = num%10
    s+=rem
    num//=10
print(s)
    