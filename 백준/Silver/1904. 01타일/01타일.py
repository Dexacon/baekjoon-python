import sys
def tile(n):
    result = [1]*(n+1)
    for i in range(2,n+1):
        result[i] = (result[i-2] + result[i-1])%15746
    return result[n]
n = int(sys.stdin.readline())
print(tile(n))