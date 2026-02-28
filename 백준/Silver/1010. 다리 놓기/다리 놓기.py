import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    top = 1
    bottom = 1
    for i in range(N):
        top *= M
        M -= 1
    for i in range(N):
        bottom *= N
        N -= 1
    print(top//bottom)