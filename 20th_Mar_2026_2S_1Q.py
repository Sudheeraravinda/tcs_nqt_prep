n = int(input())
pairs = []
for i in range(n):
    a, b = map(int, input().split())
    pairs.append((a, b))


pairs.sort(key=lambda x: (x[0], x[1]))
for p in pairs:
    print(p,end="")