import sys
input = sys.stdin.readline
N = int(input())
Chongchong = set()
Chongchong.add('ChongChong')
for i in range(N):
    X,Y = input().rstrip().split()
    if X in Chongchong and Y not in Chongchong:
        Chongchong.add(Y)
    elif Y in Chongchong and X not in Chongchong:
        Chongchong.add(X)
print(len(Chongchong))