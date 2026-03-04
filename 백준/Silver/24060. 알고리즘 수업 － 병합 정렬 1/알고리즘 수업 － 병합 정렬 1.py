import sys
input = sys.stdin.readline
A,K = map(int,input().split())
nums = list(map(int,input().split()))
cnt = 0
def merge_sort(X):
    if len(X) <= 1:
        return X
    else:
        mid = (len(X)+1)//2
        left = merge_sort(X[:mid])
        right = merge_sort(X[mid:])
    return merge(left,right)
def merge(left,right):
    global cnt
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            cnt += 1
            if cnt == K:
                print(left[i])
            i += 1
        else:
            result.append(right[j])
            cnt += 1
            if cnt == K:
                print(right[j])
            j += 1
    for x in range(i,len(left)):
        result.append(left[x])
        cnt += 1
        if cnt == K:
            print(left[x])
    for x in range(j,len(right)):
        result.append(right[x])
        cnt += 1
        if cnt == K:
            print(right[x])
    return result
merge_sort(nums)
if cnt < K:
    print(-1)