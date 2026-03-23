import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N,M = map(int,input().split())
    pile = list(map(int,input().split()))
    printer = deque((j,i) for i,j in enumerate(pile))
    cnt = 0
    X = printer[M]
    while True:
        if printer[0] == max(printer, key=lambda x: x[0]):
            if printer[0] == X:
                cnt+=1
                break
            cnt+=1
            printer.popleft()
        else:
            printer.append(printer.popleft())
    print(cnt)