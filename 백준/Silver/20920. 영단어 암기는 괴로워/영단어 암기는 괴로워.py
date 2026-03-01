import sys
input = sys.stdin.readline
N,M = map(int,input().split())
result = dict()
for _ in range(N):
    X = input().rstrip()
    if len(X) >= M:
        if X in result:
            result[X] += 1
        else:
            result[X] = 1
dictionary = sorted(result.keys(),key=lambda x:(-result[x],-len(x),x))
for i in dictionary:
    print(i)