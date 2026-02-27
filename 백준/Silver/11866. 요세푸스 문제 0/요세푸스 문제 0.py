import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int,input().split())
people = deque(range(1,N+1))
result = []
while len(people) > 0:
    for i in range(1,K+1):
        if i == K:
            result.append(str(people.popleft()))
        else:
            people.append(people.popleft())
print(f'<{", ".join(result)}>')