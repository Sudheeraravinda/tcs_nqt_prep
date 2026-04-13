inc=float(input())
e={}
exp=0
while True:
    exp_t=input()
    exp_t.lower()
    if exp_t == "done":
        break
    rate=float(input())
    if exp_t in e:
        e[exp_t] += rate
    else:
        e[exp_t]=rate
    exp+=rate
s=inc-exp
print("Income:",inc)
print("Expenditure:",exp)
print("Savings:",s)
print("/n printing all expenditures/n")
for i,j in e.items():
    print(f"{i}:{j}")


    