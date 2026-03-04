import sys
input = sys.stdin.readline
T = int(input())

def recursion(x,l,r):
    global cnt
    if l>=r:
        cnt += 1
        return 1
    elif x[l] != x[r]:
        cnt += 1
        return 0
    else:
        cnt += 1
        return recursion(x,l+1,r-1)

for _ in range(T):
    cnt = 0
    S = input().rstrip()
    print(recursion(S,0,len(S)-1),cnt)