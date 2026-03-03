import sys
input = sys.stdin.readline
def Fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return Fibonacci(x-2) + Fibonacci(x-1)
N = int(input())
print(Fibonacci(N))
