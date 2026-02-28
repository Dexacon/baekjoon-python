import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
result = deque()
for i in range(N):
    X = list(map(int,input().split()))
    match X[0]:
        case 1:
            result.appendleft(X[1])
        case 2:
            result.append(X[1])
        case 3:
            if result:
                print(result.popleft())
            else:
                print(-1)
        case 4:
            if result:
                print(result.pop())
            else:
                print(-1)
        case 5:
            print(len(result))
        case 6:
            if result:
                print(0)
            else:
                print(1)
        case 7:
            if result:
                print(result[0])
            else:
                print(-1)
        case 8:
            if result:
                print(result[-1])
            else:
                print(-1)