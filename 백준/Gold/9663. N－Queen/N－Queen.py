import sys
N = int(sys.stdin.readline())
cnt = 0
chess = [0] * N
def NQueen(depth):
    global cnt
    if depth == N:
        cnt += 1
        return
    for i in range(N):
        if is_valid(depth,i):
            chess[depth] = i
            NQueen(depth+1)
    return
def is_valid(depth,col):
    for i in range(depth):
        if abs(chess[i] - col) == abs(i - depth):
            return False
        if col == chess[i]:
            return False
    return True
NQueen(0)
print(cnt)
