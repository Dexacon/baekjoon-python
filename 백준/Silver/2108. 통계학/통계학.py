import sys
input = sys.stdin.readline
N = int(input())
dic = {}
nums = []
for i in range(N):
    X = int(input())
    nums.append(X)
    if X in dic:
        dic[X] += 1
    else:
        dic[X] = 1
item = list(dic.items())
nums.sort()
item.sort(key= lambda x: (-x[1],x[0]))
print(round(sum(nums)/N))
print(nums[N//2])
if len(item) > 1 and item[0][1] == item[1][1]:
    print(item[1][0])
else:
    print(item[0][0])
print(nums[-1]-nums[0])