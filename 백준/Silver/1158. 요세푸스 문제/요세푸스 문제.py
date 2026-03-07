import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int,input().split())
people = deque(i for i in range(1,N+1))
result = []
while people:
    for i in range(K-1):
        people.append(people.popleft())
    result.append(people.popleft())
print(f'<{', '.join(map(str,result))}>')