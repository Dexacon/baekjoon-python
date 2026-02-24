import sys
input = sys.stdin.readline
N = int(input())
result = []
for i in range(N):
    x = list(map(int,input().split()))
    match x[0]:
        case 1:
            result.append(x[1])
        case 2:
            if len(result)>0:
                print(result.pop())
            else:
                print(-1)
        case 3:
            print(len(result))
        case 4:
            if len(result)>0:
                print(0)
            else:
                print(1)
        case 5:
            if len(result)>0:
                print(result[-1])
            else:
                print(-1)
        