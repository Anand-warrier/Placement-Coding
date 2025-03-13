n = int(input())
m = int(input())
mat = [list(map(int, input().split())) for i in range(n)]
c = 0

for row in mat:
    for num in row:
        if num < 0:
            c += 1
        else:
            break

print(c)
