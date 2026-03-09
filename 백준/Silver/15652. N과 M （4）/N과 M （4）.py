import sys
N,M = map(int,input().split())
picked = [0] * M
result = []
def dfs(start,depth):
    if depth == M:
        result.append(' '.join(map(str,picked)))
        return
    for i in range(start,N+1):
        picked[depth] = i
        dfs(start,depth+1)
        start += 1
    return
dfs(1,0)
print('\n'.join(result))