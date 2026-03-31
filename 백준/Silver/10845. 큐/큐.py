import sys
from collections import deque
input = sys.stdin.readline
result = deque()
N = int(input())
for i in range(N):
    x = list(input().split())
    match x[0]:
        case 'push':
            result.append(x[1])
        case 'pop':
            if not result:
                print(-1)
            else:
                print(result.popleft())
        case 'size':
            print(len(result))
        case 'empty':
            if result:
                print(0)
            else:
                print(1)
        case 'front':
            if not result:
                print(-1)
            else:
                print(result[0])
        case 'back':
            if not result:
                print(-1)
            else:
                print(result[-1])