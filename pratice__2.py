n= int(input())
arr = list(map(int,input().split()))
freq = {}
for i in arr:
    freq[i] = freq.get(i , 0) + 1
for j in range(n):
    for k in range(j,n):
        if freq[arr[j]] > freq[arr[k]]:
            arr[j], arr[k] = arr[k] , arr[j]
        
print(arr)