import sys,itertools
N,M = map(int,sys.stdin.readline().split())
nums = [i for i in range(1,N+1)]
result = list(itertools.permutations(nums,M))
for i in result:
    print(' '.join(map(str,i)))