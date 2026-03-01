import sys
input = sys.stdin.readline
N,M = map(int,input().split())
dictionary = dict()
for _ in range(N):
    X = input().rstrip()
    if len(X) >= M:
        if X in dictionary:
            dictionary[X] += 1
        else:
            dictionary[X] = 1
result = sorted(dictionary.keys(),key=lambda x:(-dictionary[x],-len(x),x))
for i in result:
    print(i)