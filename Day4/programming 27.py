n = int(input())
prices = list(map(int, input().split()))
longest = []
current = [prices[0]]

for i in range(1, n):
    if prices[i] > prices[i - 1]:
        current.append(prices[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [prices[i]]

if len(current) > len(longest):
    longest = current

print(*longest)
