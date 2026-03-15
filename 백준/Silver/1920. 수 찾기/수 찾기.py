import sys
from collections import deque
N = int(sys.stdin.readline())
x = set(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
y = map(int,sys.stdin.readline().split())
for i in y:
    if i in x:
        print(1)
    else:
        print(0)