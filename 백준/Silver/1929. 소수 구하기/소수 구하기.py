import sys
def DecimalCheck(a):
    if a < 2:
        return False
    for i in range(2,int(a**(0.5))+1):
        if a % i == 0:
            return False
    return True
input = sys.stdin.readline
M,N = map(int,input().split())
result = [True] * (N+1)
result[0] = result[1] = False
for i in range(2,int(N**0.5)+1):
    if result[i]:
        for j in range(i*i,N+1,i):
            result[j] = False
for i in range(M,N+1):
    if result[i]:
        print(i)