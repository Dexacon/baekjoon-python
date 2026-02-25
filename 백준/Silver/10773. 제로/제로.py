import sys
input = sys.stdin.readline
K = int(input())
result = []
for i in range(K):
    n = int(input())
    try:
        if n == 0:
            result.pop()
        else:
            result.append(n)
    except IndexError:
        print('잘못된 입력입니다.')
print(sum(result))
