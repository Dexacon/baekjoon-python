import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = int(input())
C = map(int,input().split())
queuestack = deque()
for i in range(N):
    if A[i] == 0:
        queuestack.append(B[i])
for i in C:
    queuestack.appendleft(i)
    print(queuestack.pop())