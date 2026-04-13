def prime(a):
    if a == 1:
        return False
    elif a == 2 :
        return True
    else:
        for i in range(2,int(a**0.5 + 1)):
            if a % i == 0:
                return False
            return True
        
n= int(input("Enter number :"))
s=0
while n > 0 :
    rem = n % 10
    s+=rem
    n = n // 10
    
if prime(s) :
    print("Googly prime number")
else:
    print("Not a googly prime")
       
       
            
            
            
        