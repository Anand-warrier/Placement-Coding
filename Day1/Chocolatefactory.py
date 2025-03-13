n=int(input())
arr=[int(i) for i in input().split()]
for i in arr:
    if i==0:
        arr.remove(i)
        arr.append(0)
print(arr)
