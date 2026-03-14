import sys
N,M = map(int,sys.stdin.readline().split())
dictionary = dict()
for i in range(N):
    x,y = sys.stdin.readline().rstrip().split()
    dictionary[x] = y
for i in range(M):
    z = sys.stdin.readline().rstrip()
    print(dictionary[z])