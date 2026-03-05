import sys
def star(N):
    if N == 1:
        return ['*']
    else:
        sub = star(N//3)
        blank = [' '*(N//3)] * (N//3)
        return merge(sub,blank)
def merge(sub,blank):
    top = [a+b+c for a,b,c in zip(sub,sub,sub)]
    midle = [a+b+c for a,b,c in zip(sub,blank,sub)]
    bottom = [a+b+c for a,b,c in zip(sub,sub,sub)]
    return top+midle+bottom
N = int(sys.stdin.readline())
print('\n'.join(star(N)))