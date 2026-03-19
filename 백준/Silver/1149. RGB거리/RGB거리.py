import sys
input = sys.stdin.readline
prices = []
N = int(input())
for _ in range(N):
    color_price = list(map(int,input().split()))
    prices.append(color_price)
for i in range(1,N):
    prices[i][0] += min(prices[i-1][1],prices[i-1][2])
    prices[i][1] += min(prices[i-1][0],prices[i-1][2])
    prices[i][2] += min(prices[i-1][0],prices[i-1][1])
print(min(prices[N-1]))
