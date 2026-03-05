import sys
N,M = map(int,sys.stdin.readline().split())
pick = [0] * M
nums = [False] * (N+1)
result = []
def dfs(depth):
    if depth == M:
        result.append(" ".join(map(str,pick)))
        return
    for i in range(1,N+1):
        if nums[i]:
            continue
        else:
            nums[i] = True
            pick[depth] = i
            dfs(depth + 1)
            nums[i] = False
dfs(0)
print('\n'.join(result))