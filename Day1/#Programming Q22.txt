#Programming Q22
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
odd=0

for i in arr:
    if i%2!=0:
        odd+=1
if odd:
    print("Odd Elements:",odd)
else:
    print("No odd elements are present")