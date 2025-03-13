nums = list(map(int, input().split(",")))
k = int(input())
nums.sort()
min_u = float("inf")
res = []

for i in range(len(nums) - k + 1):
    u = nums[i + k - 1] - nums[i]
    if u < min_u:
        min_u = u
        res = nums[i:i + k]

print(*res)
