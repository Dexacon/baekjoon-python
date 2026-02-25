import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    n =input().rstrip()
    cnt1 = 0
    cnt2 = 0
    check = True
    for i in n:
        if cnt1 != 0 and cnt1 == cnt2:
            cnt1 = 0
            cnt2 = 0
        if cnt1 == 0 and i != '(':
            print('NO')
            check = False
            break
        
        if i == '(':
            cnt1 += 1
        elif i == ')':
            cnt2 += 1
    if check:
        if cnt1 != 0 and cnt1 == cnt2:
            print('YES')
        else:
            print('NO')