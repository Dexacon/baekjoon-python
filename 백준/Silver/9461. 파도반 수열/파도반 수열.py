import sys
T = int(sys.stdin.readline())
def wave(n):
    result = [1]*(n+1)
    for i in range(4,n+1):
        result[i] = result[i-3] + result[i-2]
    return result[n]
for i in range(T):
    N = int(sys.stdin.readline())
    print(wave(N))
