#Programming Q20
n=int(input())
arr=list(map(int,input().split()))
set1=set()
for i in arr:
    if i not in set1:
        set1.add(i)
    else:
        print("true")
        exit(0)
print("false")        