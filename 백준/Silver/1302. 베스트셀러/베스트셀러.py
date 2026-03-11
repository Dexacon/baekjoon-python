import sys
N = int(sys.stdin.readline())
book = dict()
for i in range(N):
    x = sys.stdin.readline().rstrip()
    if x in book:
        book[x] += 1
    else:
        book[x] = 1
result = sorted(book.items(),key= lambda x: (-x[1],x[0]))
print(result[0][0])