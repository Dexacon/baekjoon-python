import sys
input = sys.stdin.readline
N,M = map(int,input().split())
picked = [0] * M
nums = [False] * (N+1)
result = []
def dfs(depth):
    if depth == M:
        result.append(' '.join(map(str,picked)))
        return
    for i in range(1,N+1):
        if nums[i]:
            continue
        picked[depth] = i
        dfs(depth+1)
    return
dfs(0)
print('\n'.join(result))