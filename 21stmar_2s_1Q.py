t=int(input())
bill=0
if t<=2:
    bill = t*100
elif t<=5:
    bill = (200+(t-2)*50)
else:
    bill= (200+150+(t-5)*20)
print(bill)
    