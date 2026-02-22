import sys
def DecimalCheck(a):
    if a < 2:
        return False
    for i in range(2,int(a**(0.5))+1):
        if a % i == 0:
            return False
    return True
T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    while True:
        if DecimalCheck(n):
            break
        n += 1
    print(n)
