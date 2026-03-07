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
        elif depth != 0 and picked[depth-1] > i:
            continue
        nums[i] = True
        picked[depth] = i
        dfs(depth+1)
        nums[i] = False
    return
dfs(0)
print('\n'.join(result))