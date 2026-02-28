import itertools
N,K = map(int,input().split())
X = list(range(1,N+1))
print(len(list(itertools.combinations(X,K))))