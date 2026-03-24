import sys,itertools
input = sys.stdin.readline
N = int(input())
K = int(input())
card = []
putcard = set()
for i in range(N):
    X = input().rstrip()
    card.append(X)
for i in itertools.permutations(card,K):
    putcard.add(''.join(i))
print(len(putcard))
