import sys
input = sys.stdin.readline
N = int(input())
students = list(map(int,input().split()))
students.reverse()
sort = []
cnt = 0
for i in range(1,N+1):
    for j in reversed(students):
        if j == i:
            cnt += 1
            students.pop()
            break
        elif len(sort) != 0 and sort[-1] == i:
            cnt += 1
            sort.pop()
            break
        else:
             sort.append(students.pop())
sort.reverse()
if sort == sorted(sort):
     cnt += len(sort)
if cnt == N:
     print('Nice')
else:
     print('Sad')
