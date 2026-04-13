s=input()
c=0
ans = " "
for i in s:
    if i == '1':
        c+=1
    else:
        if c > 0 :
            print(chr(96+c), end = "")
            c=0

        