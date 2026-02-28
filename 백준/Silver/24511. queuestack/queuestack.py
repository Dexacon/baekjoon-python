import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = int(input())
C = list(map(int,input().split()))
result = []
queuestack = deque()
for i in range(N):
    if A[i] == 0:
        queuestack.append(B[i])
for i in C:
    queuestack.appendleft(i)
    result.append(queuestack.pop())
print(*result)