import sys
from collections import deque
N = int(sys.stdin.readline())
result = deque()
for i in range(N):
    x = list(sys.stdin.readline().rstrip().split())
    match x[0]:
        case 'push':
            result.append(x[1])
        case 'pop':
            if result:
                print(result.pop())
            else:
                print(-1)
        case 'size':
            print(len(result))
        case 'empty':
            if result:
                print(0)
            else:
                print(1)
        case 'top':
            if result:
                print(result[-1])
            else:
                print(-1)
