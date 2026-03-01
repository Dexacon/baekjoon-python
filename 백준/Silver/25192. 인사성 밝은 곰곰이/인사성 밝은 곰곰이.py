import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
for _ in range(N): 
    X = input().rstrip() 
    if X == 'ENTER':
        gomgom = set()
    else:
        if X in gomgom:
            continue
        else:
            gomgom.add(X)
            cnt += 1
print(cnt)