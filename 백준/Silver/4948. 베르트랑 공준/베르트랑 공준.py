import sys
input = sys.stdin.readline
nums = []
while True:
    n = int(input())
    if n == 0:
        break
    nums.append(n)
maxcheck = max(nums)   
result = [True] * (2*maxcheck+1)
result[0] = result[1] = False
for i in range(2,int((2*maxcheck)**0.5)+1):
    if result[i]:
        for j in range(i*i,len(result),i):
            result[j] = False
for i in nums:
    print(result[i+1:2*i+1].count(True))