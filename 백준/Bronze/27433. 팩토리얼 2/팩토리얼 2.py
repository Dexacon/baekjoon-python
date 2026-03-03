import sys
input = sys.stdin.readline
N = int(input())
result = 1
def factorial(x):
    global result
    result *= x
    if x > 1:
        x-=1
        return factorial(x)
    elif x == 0:
        return 1
    return result
print(factorial(N))