import sys
input = sys.stdin.readline
result = [True] * 1000001
result[0] = result[1] = False
for i in range(2,int(1000000**0.5)+1):
    if result[i]:
        for j in range(i*i,len(result),i):
            result[j] = False
T = int(input())
for i in range(T):
    n = int(input())
    count = 0
    for j in range(1,n//2+1):
        if result[j] and result[n-j]:
            count += 1
    print(count)