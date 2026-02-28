import sys
N = int(sys.stdin.readline())
sang = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
me = list(map(int,sys.stdin.readline().split()))
dic = {}
for i in range(N):
    if sang[i] not in dic:
        dic[sang[i]] = 1
    else:
        dic[sang[i]] += 1
for i in me:
    if i in dic:
        print(dic[i],end=' ')
    else:
        print(0,end=' ')     