import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
que = deque([])
for i in range(N):
    X = list(input().rstrip().split())    
    match X[0]:
        case 'push':
            que.append(X[1])
        case 'pop':
            if que:
                print(que.popleft())
            else:
                print(-1)
        case 'size':
            print(len(que))
        case 'empty':
            if que:
                print(0)
            else:
                print(1)
        case 'front':
            if que:
                print(que[0])
            else:
                print(-1)
        case 'back':
            if que:
                print(que[-1])
            else:
                print(-1)