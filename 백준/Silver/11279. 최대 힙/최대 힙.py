import sys,heapq
input = sys.stdin.readline
N = int(input())
maxheap = []
for i in range(N):
    x = int(input())
    if x == 0:
        if maxheap:
            print(-heapq.heappop(maxheap))
        else:
            print(0)
    else:
        heapq.heappush(maxheap,-x)
