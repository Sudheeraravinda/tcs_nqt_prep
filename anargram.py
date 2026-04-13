s1=input().replace(" ","").lower()
s2=input().replace(" ","").lower()
if len(s1)!=len(s2):
    print("Not a anargram")
else:
    if sorted(s1)==sorted(s2):
        print("Anargram")
    else:
        print("Not a anargram")

    
    