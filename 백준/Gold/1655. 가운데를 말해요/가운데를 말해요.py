import sys
import heapq

input = sys.stdin.readline
N = int(input())

left_nums = []
right_nums = []

for _ in range(N):
    x = int(input())
    
    if len(left_nums) == len(right_nums):
        heapq.heappush(left_nums, -x)
    else:
        heapq.heappush(right_nums, x)
        
    if right_nums and (-left_nums[0] > right_nums[0]):
        left_val = -heapq.heappop(left_nums)
        right_val = heapq.heappop(right_nums)
        
        heapq.heappush(left_nums, -right_val)
        heapq.heappush(right_nums, left_val)
        
    print(-left_nums[0])