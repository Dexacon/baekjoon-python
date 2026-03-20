import sys
input = sys.stdin.readline
N = int(input())
triangle = []
for i in range(N):
    x = list(map(int,input().split()))
    triangle.append(x)
for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == i:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j-1])
print(max(triangle[N-1]))