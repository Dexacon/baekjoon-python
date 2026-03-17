import sys
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
max_sum = nums[0]
current_sum = nums[0]
for i in range(1, len(nums)):
    current_sum = max(current_sum + nums[i], nums[i])
    max_sum = max(max_sum, current_sum)
print(max_sum)