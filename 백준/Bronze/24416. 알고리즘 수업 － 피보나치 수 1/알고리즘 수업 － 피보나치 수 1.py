import sys
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-2) + fib(n-1)
def fibonacci(n):
    f = [0] * (n+1)
    f[1] = 1
    f[2] = 1
    for i in range(3,n+1):
        f[i] = f[i-2] + f[i-1]
    return f[n]
n = int(sys.stdin.readline())
print(fibonacci(n),n-2)