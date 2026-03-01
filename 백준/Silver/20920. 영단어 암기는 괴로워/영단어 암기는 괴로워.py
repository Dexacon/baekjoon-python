import sys
input = sys.stdin.readline
N,M = map(int,input().split())
result = dict()
dictionary = list()
for _ in range(N):
    X = input().rstrip()
    if len(X) >= M:
        if X in result:
            result[X] += 1
        else:
            result[X] = 1
for a,b in result.items():
    dictionary.append((a,b))
dictionary.sort(key= lambda x:(-x[1],-len(x[0]),x[0]))
for i in range(len(dictionary)):
    print(dictionary[i][0])
