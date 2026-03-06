import sys
def hanoi(n,start,end,case):
    if n == 1:
        print(start,end)
        return
    hanoi(n-1,start,case,end)
    print(start,end)
    hanoi(n-1,case,end,start)
    return
N = int(sys.stdin.readline())
print(2**N-1)
hanoi(N,1,3,2)