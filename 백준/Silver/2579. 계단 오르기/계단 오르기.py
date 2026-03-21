import sys
input = sys.stdin.readline
N = int(input())
stair = []
for i in range(N):
    stair.append(int(input()))
dp = [[0] * 2 for _ in range(N)]
dp[0][0] = stair[0]
if N >= 2:
    dp[1][0] = stair[1]
    dp[1][1] = dp[0][0] + stair[1]
for i in range(2,N):
    dp[i][0] = max(dp[i-2][0],dp[i-2][1]) + stair[i]
    dp[i][1] = dp[i-1][0] + stair[i]
print(max(dp[N-1][0],dp[N-1][1]))