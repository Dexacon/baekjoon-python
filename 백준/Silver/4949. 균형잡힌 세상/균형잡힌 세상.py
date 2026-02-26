import sys
while True:
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break
    stack = []
    check = True
    for i in line:
        if len(stack) == 0:
            if i == '(':
                stack.append(i)
            elif i == '[':
                stack.append(i)
            elif i == ')':
                print('no')
                check = False
                break
            elif i == ']':
                print('no')
                check = False
                break
        else:
            if i == ')':
                if stack[-1] == '(':
                    stack.pop()
                elif stack[-1] == '[':
                    print('no')
                    check = False
                    break
                else:
                    stack.append(i)
            elif i == ']':
                if stack[-1] == '[':
                    stack.pop()
                elif stack[-1] == '(':
                    print('no')
                    check = False
                    break
                else:
                    stack.append(i)
            if i == '(':
                stack.append(i)
            elif i == '[':
                stack.append(i)
    if check:
        if len(stack) == 0:
            print("yes")
        else:
            print('no')    
