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
for i in range(M,N+1):
    if DecimalCheck(i):
        print(i)