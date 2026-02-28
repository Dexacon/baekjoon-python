import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
result = deque(range(1,N+1))
nums = list(map(int,input().split()))
first = True
x = 0
for i in range(N):
    if first:
        print(result.popleft(),end=' ')        
        first = False
    elif nums[x] >= 0:
        for j in range(nums[x]-1):
            result.append(result.popleft())
        x = result[0] - 1
        print(result.popleft(),end=' ')
        
    else:
        for j in range(abs(nums[x])-1):
            result.appendleft(result.pop())
        x = result[-1] - 1
        print(result.pop(),end=' ')